from datetime import date

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.table import Table

from gittales.core.analyzer import ActivityAnalyzer
from gittales.core.reader import GitReader
from gittales.reports.console import DailyActivityReporter
from gittales.utils.helpers import parse_date

console = Console()
app = typer.Typer()


@app.callback()
def callback():
    """Extract insights from your git commit history"""
    pass


@app.command()
def daily_report(
    repo: str = typer.Option(".", "--repo", "-r", help="Path to the git repository"),
    user: str = typer.Option(..., "--user", "-u", help="Username to filter commits"),
    date_str: str = typer.Option(None, "--date", "-d", help="Date for analysis (YYYY-MM-DD), defaults to today"),
):
    """
    Analyze the given repository and produce a daily activity report for a specific user.
    """
    # Determine the analysis date
    analysis_date = parse_date(date_str) if date_str else date.today()

    # Read commit history
    reader = GitReader()
    commits = reader.get_commits(repo, user, analysis_date)
    if not commits:
        typer.echo("No commits found for the specified date/user.")
        raise typer.Exit()

    # Process commits into activity entries
    analyzer = ActivityAnalyzer()
    activities = analyzer.analyze(commits)

    # Report using the console reporter
    reporter = DailyActivityReporter()
    reporter.report(activities)


@app.command()
def analyze(
    days: int = typer.Option(14, "--days", "-d", help="Days of history to analyze"),
    repos: list[str] = typer.Option(None, "--repo", "-r", help="Git repositories to analyze"),
):
    """Analyze git repositories and generate insights."""
    repos = repos or ["current directory"]
    console.print(Panel("[bold blue]GitTales[/bold blue] is analyzing your coding story..."))

    # Sample data to show off Rich formatting
    sample_commits = [
        {"repo": "gittales", "date": "2025-03-08", "message": "Initial commit", "author": "Patrick", "files": 5},
        {"repo": "gittales", "date": "2025-03-09", "message": "Add CLI interface", "author": "Patrick", "files": 2},
        {"repo": "other-project", "date": "2025-03-07", "message": "Fix login bug", "author": "Patrick", "files": 1},
    ]

    # Create a beautiful table with Rich
    table = Table(title="Recent Commits")
    table.add_column("Date", style="cyan")
    table.add_column("Repository", style="green")
    table.add_column("Message", style="bright_white")
    table.add_column("Files", justify="right", style="purple")

    for commit in sample_commits:
        table.add_row(commit["date"], commit["repo"], commit["message"], str(commit["files"]))

    # Show processing work with a progress bar
    for repo in track(repos, description="Processing repositories"):
        # This simulates work happening
        console.print(f"Analyzing [bold green]{repo}[/bold green]...")

    console.print(table)

    # Summary panel with stats
    stats_text = """
    [bold cyan]Your Coding Summary:[/bold cyan]

    🔥 [bold]Most Active Day:[/bold] Thursday (8 commits)
    💻 [bold]Focus Project:[/bold] gittales (65% of commits)
    ⏰ [bold]Peak Coding Hours:[/bold] 10am - 2pm

    You've made [bold green]42[/bold green] commits across [bold green]3[/bold green] repositories in the last 14 days!
    """
    console.print(Panel(stats_text, title="GitTales Insights", border_style="green"))


def main():
    app()


if __name__ == "__main__":
    main()
