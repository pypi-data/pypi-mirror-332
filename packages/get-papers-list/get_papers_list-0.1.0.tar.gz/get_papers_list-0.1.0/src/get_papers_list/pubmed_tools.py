import requests
from lxml import etree
import re

def fetch_paper_ids(query: str, max_results: int = 10) -> list:
    """
    Fetch paper IDs from PubMed based on a query.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        paper_ids = data.get("esearchresult", {}).get("idlist", [])
        return paper_ids
    else:
        raise Exception(f"Failed to fetch papers: {response.status_code}")

def is_pharma_biotech(affiliation: str) -> bool:
    """
    Check if an affiliation is from a pharmaceutical or biotech company.
    """
    pharma_keywords = [
        "pharma", "biotech", "pharmaceutical", "biotechnology", 
        "inc.", "ltd.", "corp.", "company", "research and development", 
        "drug", "vaccine", "therapy", "biologics", "genentech", 
        "pfizer", "moderna", "astrazeneca", "novartis", "roche", 
        "johnson & johnson", "merck", "gilead", "sanofi", "bayer"
    ]
    return any(keyword.lower() in affiliation.lower() for keyword in pharma_keywords)

def extract_email(affiliation: str) -> str:
    """
    Extract email from affiliation text using regex.
    """
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    match = re.search(email_pattern, affiliation)
    return match.group(0) if match else None

def fetch_paper_details(paper_id: str, debug: bool = False) -> dict:
    """
    Fetch details for a single paper from PubMed.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": paper_id,
        "retmode": "xml"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        # Parse the XML response
        root = etree.fromstring(response.content)

        # Extract details
        paper_details = {
            "PubmedID": paper_id,
            "Title": root.findtext(".//ArticleTitle"),
            "PublicationDate": root.findtext(".//PubDate/Year"),
            "NonAcademicAuthors": [],
            "CompanyAffiliations": [],
            "CorrespondingAuthorEmail": None,
            "HasPharmaBiotechAffiliation": False  # Flag to check if paper meets the requirement
        }

        # Extract authors and affiliations
        for author in root.findall(".//Author"):
            last_name = author.findtext("LastName")
            fore_name = author.findtext("ForeName")
            affiliations = author.findall(".//AffiliationInfo/Affiliation")  # Extract all affiliations
            if last_name and fore_name:
                full_name = f"{fore_name} {last_name}"
                # Check if any affiliation is from a pharmaceutical/biotech company
                for affiliation in affiliations:
                    if affiliation.text and is_pharma_biotech(affiliation.text):
                        paper_details["NonAcademicAuthors"].append(full_name)
                        paper_details["CompanyAffiliations"].append(affiliation.text)
                        paper_details["HasPharmaBiotechAffiliation"] = True

                # Extract email for corresponding author
                if author.get("ValidYN") == "Y":
                    email = extract_email(affiliation.text if affiliation.text else "")
                    if email:
                        paper_details["CorrespondingAuthorEmail"] = email

        # Deduplicate affiliations and authors
        paper_details["CompanyAffiliations"] = list(set(paper_details["CompanyAffiliations"]))
        paper_details["NonAcademicAuthors"] = list(set(paper_details["NonAcademicAuthors"]))

        # Debug information
        if debug:
            print(f"Processed paper ID: {paper_id}")
            print(f"Title: {paper_details['Title']}")
            print(f"Non-academic authors: {paper_details['NonAcademicAuthors']}")
            print(f"Company affiliations: {paper_details['CompanyAffiliations']}")
            print(f"Corresponding author email: {paper_details['CorrespondingAuthorEmail']}")
            print("-" * 50)

        # Only return papers with at least one pharmaceutical/biotech affiliation
        if paper_details["HasPharmaBiotechAffiliation"]:
            return paper_details
        else:
            return None  # Skip papers that don't meet the requirement
    else:
        raise Exception(f"Failed to fetch paper details: {response.status_code}")