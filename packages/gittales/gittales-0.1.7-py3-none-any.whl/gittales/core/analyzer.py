from datetime import datetime, time, timezone

from .models import ActivityEntry, Commit


class ActivityAnalyzer:
    WORK_START = time(8, 0)
    WORK_END = time(17, 0)

    def analyze(self, commits: list[Commit]) -> list[ActivityEntry]:
        if not commits:
            return []

        sorted_commits = sorted(commits, key=lambda c: c.date)
        activities = []

        # Set working boundaries based on the date of the first commit.
        work_date = sorted_commits[0].date.date()
        # Make datetime objects timezone-aware using the same timezone as the commits
        commit_tz = sorted_commits[0].date.tzinfo
        working_start = datetime.combine(work_date, self.WORK_START).replace(tzinfo=commit_tz)
        working_end = datetime.combine(work_date, self.WORK_END).replace(tzinfo=commit_tz)

        # Create an activity entry from working start to first commit time.
        first_commit_time = max(sorted_commits[0].date, working_start)
        duration = (first_commit_time - working_start).total_seconds() / 60
        if duration > 0:
            activities.append(
                ActivityEntry(
                    start_time=working_start,
                    end_time=first_commit_time,
                    duration_minutes=duration,
                    commit=sorted_commits[0],
                )
            )

        # Create activity entries for intermediate commits.
        for prev, curr in zip(sorted_commits, sorted_commits[1:]):
            start = prev.date
            end = curr.date
            duration = (end - start).total_seconds() / 60
            activities.append(ActivityEntry(start_time=start, end_time=end, duration_minutes=duration, commit=curr))

        # Activity entry from the last commit to working end (if applicable).
        last_commit_time = sorted_commits[-1].date
        if last_commit_time < working_end:
            duration = (working_end - last_commit_time).total_seconds() / 60
            activities.append(
                ActivityEntry(
                    start_time=last_commit_time,
                    end_time=working_end,
                    duration_minutes=duration,
                    commit=sorted_commits[-1],
                )
            )
        return activities
