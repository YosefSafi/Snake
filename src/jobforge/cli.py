import click
import logging
from jobforge.db.session import init_db
from jobforge.search.engine import JobSearchEngine
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
def main():
    logging.basicConfig(level=logging.INFO)
    init_db()

@main.command()
@click.option("--query", help="Custom search query")
def search(query):
    """Run a job search (Agent will assist with real-time tools)."""
    console.print(f"[bold blue]Searching for jobs...[/bold blue]")
    # For now, this is a placeholder that reminds the user the Agent performs the search.
    console.print("Please use the Agent's `google_web_search` tool for real-time results.")

@main.command()
def list():
    """List all found jobs."""
    engine = JobSearchEngine()
    jobs = engine.list_jobs()
    
    if not jobs:
        console.print("[yellow]No jobs found yet.[/yellow]")
        return

    table = Table(title="Found Jobs")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Company", style="green")
    table.add_column("Location")
    table.add_column("Status")

    for job in jobs:
        table.add_row(str(job.id), job.title, job.company, job.location or "N/A", job.status)

    console.print(table)

if __name__ == "__main__":
    main()
