import click
import logging
import json
import os
from jobforge.db.session import init_db
from jobforge.search.engine import JobSearchEngine
from jobforge.search.scraper import JobScraper
from jobforge.search.matcher import MatchEngine
from jobforge.application.helper import ApplicationHelper
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
    table.add_column("Match %", style="bold yellow")
    table.add_column("Status")

    for job in jobs:
        match_str = f"{job.match_score}%" if job.match_score is not None else "N/A"
        table.add_row(str(job.id), job.title, job.company, match_str, job.status)

    console.print(table)

@main.command()
@click.option("--profile", default="profile.json", help="Path to profile JSON")
def match(profile):
    """Calculate match scores for all jobs based on profile skills."""
    if not os.path.exists(profile):
        console.print(f"[red]Profile file {profile} not found.[/red]")
        return
    
    with open(profile, "r") as f:
        profile_data = json.load(f)
    
    skills = profile_data.get("skills", [])
    matcher = MatchEngine(skills)
    engine = JobSearchEngine()
    jobs = engine.list_jobs()
    
    console.print(f"[blue]Calculating match scores for {len(jobs)} jobs...[/blue]")
    
    for job in jobs:
        if job.description:
            score = matcher.calculate_score(job.description)
            job.match_score = score
            engine.db.commit()
            console.print(f"Job {job.id}: [green]{score}%[/green] match")
        else:
            console.print(f"Job {job.id}: [yellow]Skipped (no description)[/yellow]")

    console.print("[bold green]Matching complete![/bold green]")

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
    console.print(f"Match Score: {job.match_score or 'N/A'}%")
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
    console.print("Please wait for the Agent to fetch the content...")

@main.command()
@click.argument("job_id", type=int)
@click.option("--profile", default="profile.json", help="Path to profile JSON")
def generate_letter(job_id, profile):
    """Generate a tailored cover letter for a job."""
    if not os.path.exists(profile):
        console.print(f"[red]Profile file {profile} not found.[/red]")
        return
    
    with open(profile, "r") as f:
        profile_data = json.load(f)
    
    engine = JobSearchEngine()
    job = engine.get_job(job_id)
    if not job:
        console.print(f"[red]Job {job_id} not found.[/red]")
        return
    
    helper = ApplicationHelper(profile_data)
    letter = helper.generate_cover_letter(job.title, job.company, job.description or "")
    
    filename = f"cover_letter_job_{job_id}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(letter)
    
    console.print(f"[bold green]Cover letter generated successfully: {filename}[/bold green]")
    console.print("-" * 20)
    console.print(letter)

@main.command()
@click.option("--threshold", default=20.0, help="Minimum match score to include")
def digest(threshold):
    """Show a daily digest of top matching jobs."""
    engine = JobSearchEngine()
    jobs = engine.list_jobs()
    
    top_jobs = [j for j in jobs if j.match_score is not None and j.match_score >= threshold]
    top_jobs.sort(key=lambda x: x.match_score, reverse=True)
    
    if not top_jobs:
        console.print(f"[yellow]No jobs found with match score >= {threshold}%.[/yellow]")
        return

    console.print(f"[bold green]Daily Job Digest (Top Matches >= {threshold}%)[/bold green]")
    table = Table()
    table.add_column("Match %", style="bold yellow")
    table.add_column("Title", style="magenta")
    table.add_column("Company", style="green")
    table.add_column("Link")

    for job in top_jobs:
        table.add_row(f"{job.match_score}%", job.title, job.company, job.link)

    console.print(table)

if __name__ == "__main__":
    main()
