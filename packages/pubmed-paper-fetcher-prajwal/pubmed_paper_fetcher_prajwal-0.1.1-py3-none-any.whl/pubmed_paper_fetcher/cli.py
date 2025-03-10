import typer
from pubmed_paper_fetcher.fetch_papers import fetch_paper_ids, fetch_paper_details, save_to_csv



app = typer.Typer()

@app.command()
def search(query: str, output: str = "results.csv"):
    """
    Fetches PubMed papers based on a search query and saves them to a CSV file.
    """
    typer.echo(f"Fetching PubMed papers for query: {query}")
    
    paper_ids = fetch_paper_ids(query, max_results=10)
    papers = fetch_paper_details(paper_ids)
    save_to_csv(papers, output)

    typer.echo(f"Results saved to {output}")


if __name__ == "__main__":
    app()
