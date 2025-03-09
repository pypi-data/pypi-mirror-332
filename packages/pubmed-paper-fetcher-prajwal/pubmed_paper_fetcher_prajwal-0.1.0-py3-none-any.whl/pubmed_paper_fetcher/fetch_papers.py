import requests
import xml.etree.ElementTree as ET

# PubMed API Endpoints
SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_paper_ids(query: str, max_results: int = 10):
    """Fetch research paper IDs from PubMed based on a query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(SEARCH_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")

    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])


def fetch_paper_details(paper_ids: list):
    """Fetch detailed information for a list of PubMed paper IDs."""
    if not paper_ids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }
    response = requests.get(FETCH_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching details: {response.status_code}")

    return parse_pubmed_xml(response.text)


def parse_pubmed_xml(xml_data: str):
    """Parse XML response from PubMed and extract details."""
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        paper = {}
        paper["PubmedID"] = article.findtext(".//PMID")
        paper["Title"] = article.findtext(".//ArticleTitle")
        paper["Publication Date"] = article.findtext(".//PubDate/Year")

        # Extract author information
        authors = []
        non_academic_authors = []
        company_affiliations = []

        for author in article.findall(".//Author"):
            last_name = author.findtext("LastName")
            first_name = author.findtext("ForeName")
            affiliation = author.findtext(".//Affiliation")
            
            if last_name and first_name:
                full_name = f"{first_name} {last_name}"
                authors.append(full_name)

            # Check if affiliation contains company-related terms
            if affiliation and not any(x in affiliation.lower() for x in ["university", "college", "institute", "hospital"]):
                non_academic_authors.append(full_name)
                company_affiliations.append(affiliation)

        paper["Non-academic Authors"] = ", ".join(non_academic_authors) or "None"
        paper["Company Affiliations"] = ", ".join(company_affiliations) or "None"

        # Extract corresponding author email if available
        corresponding_email = article.findtext(".//ELocationID[@EIdType='doi']")
        paper["Corresponding Author Email"] = corresponding_email or "Not Available"

        papers.append(paper)

    return papers

import csv

def save_to_csv(papers: list, filename: str = "papers.csv"):
    """Save fetched papers to a CSV file."""
    if not papers:
        print("No papers to save.")
        return

    headers = ["PubmedID", "Title", "Publication Date", 
               "Non-academic Authors", "Company Affiliations", 
               "Corresponding Author Email"]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(papers)

    print(f"Results saved to {filename}")


import argparse

def main():
    """Main function to handle command-line arguments and run the script."""
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, default="papers.csv", help="Output CSV file name")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print(f"DEBUG: Searching for papers with query: '{args.query}'")

    print("Fetching PubMed papers...")
    paper_ids = fetch_paper_ids(args.query, max_results=5)

    if not paper_ids:
        print("No papers found.")
    else:
        papers = fetch_paper_details(paper_ids)
        save_to_csv(papers, args.file)

if __name__ == "__main__":
    main()

