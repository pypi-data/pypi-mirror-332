from rich.console import Console
from rich.table import Table


class DailyActivityReporter:
    def report(self, activities: list) -> None:
        console = Console()
        table = Table(title="Daily Activity Report")
        table.add_column("Start Time", style="cyan")
        table.add_column("End Time", style="cyan")
        table.add_column("Duration (min)", justify="right", style="magenta")
        table.add_column("Commit Message", style="green")

        total_duration = 0.0
        for act in activities:
            start_str = act.start_time.strftime("%H:%M")
            end_str = act.end_time.strftime("%H:%M")
            duration_str = f"{act.duration_minutes:.1f}"
            total_duration += act.duration_minutes
            table.add_row(start_str, end_str, duration_str, act.commit.message)

        console.print(table)
        console.print(f"\nTotal Time Spent: {total_duration:.1f} minutes\n")
