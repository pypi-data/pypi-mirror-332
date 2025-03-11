import argparse
import pandas as pd
from .pubmed_api import fetch_paper_ids, fetch_paper_details

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Fetch research papers from PubMed with pharmaceutical/biotech affiliations.",
        epilog="Example: poetry run get-papers-list 'COVID-19 vaccine' --file output.csv"
    )
    parser.add_argument("query", type=str, help="PubMed query to search for papers.")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information during execution.")
    parser.add_argument("-f", "--file", type=str, help="Filename to save the results as a CSV file.")
    args = parser.parse_args()

    # Fetch paper IDs
    if args.debug:
        print(f"Fetching papers for query: {args.query}")
    paper_ids = fetch_paper_ids(args.query)

    # Fetch and filter papers
    filtered_papers = []
    for paper_id in paper_ids:
        try:
            paper_details = fetch_paper_details(paper_id, debug=args.debug)
            if paper_details:  # Only include papers with pharmaceutical/biotech affiliations
                filtered_papers.append(paper_details)
        except Exception as e:
            print(f"Error fetching details for paper {paper_id}: {e}")

    # Convert results to a DataFrame
    df = pd.DataFrame(filtered_papers)

    # Save to CSV or print to console
    if args.file:
        df.to_csv(args.file, index=False)
        print(f"Results saved to {args.file}")
    else:
        print(df)

if __name__ == "__main__":
    main()