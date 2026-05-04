import click
import logging
from jobforge.db.session import init_db
from jobforge.search.engine import JobSearchEngine
from jobforge.search.scraper import JobScraper
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

@main.command()
@click.argument("job_id", type=int)
@click.argument("status")
def status(job_id, status):
    """Update the status of a job (e.g., 'Applied', 'Rejected')."""
    engine = JobSearchEngine()
    if engine.update_job_status(job_id, status):
        console.print(f"[green]Job {job_id} status updated to '{status}'.[/green]")
    else:
        console.print(f"[red]Job {job_id} not found.[/red]")

@main.command()
@click.argument("job_id", type=int)
def detail(job_id):
    """Show detailed information for a specific job."""
    engine = JobSearchEngine()
    job = engine.get_job(job_id)
    if not job:
        console.print(f"[red]Job {job_id} not found.[/red]")
        return

    console.print(f"[bold cyan]Job Details (ID: {job.id})[/bold cyan]")
    console.print(f"Title: {job.title}")
    console.print(f"Company: {job.company}")
    console.print(f"Location: {job.location}")
    console.print(f"Link: {job.link}")
    console.print(f"Source: {job.source}")
    console.print(f"Status: {job.status}")
    console.print(f"Match Score: {job.match_score or 'N/A'}")
    console.print(f"Last Checked: {job.last_checked}")
    console.print("-" * 20)
    console.print(f"Description:\n{job.description or 'No description available.'}")

@main.command()
@click.argument("job_id", type=int)
def fetch_desc(job_id):
    """Fetch and save the description for a specific job."""
    engine = JobSearchEngine()
    job = engine.get_job(job_id)
    if not job:
        console.print(f"[red]Job {job_id} not found.[/red]")
        return
    
    console.print(f"[bold blue]Fetching description for Job {job_id}: {job.link}...[/bold blue]")
    # The Agent will now use WebFetch based on this intent.
    console.print("Please wait for the Agent to fetch the content...")

if __name__ == "__main__":
    main()
