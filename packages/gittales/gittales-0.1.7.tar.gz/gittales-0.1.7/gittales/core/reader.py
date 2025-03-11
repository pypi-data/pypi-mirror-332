from datetime import date

from git import Repo  # GitPython will be used

from .models import Commit


class GitReader:
    def get_commits(self, repo_path: str, user: str, analysis_date: date):
        try:
            repo = Repo(repo_path)
        except Exception as e:
            raise ValueError(f"Invalid repository path: {repo_path}") from e

        commits = []
        for commit in repo.iter_commits():
            commit_datetime = commit.committed_datetime
            if commit.author.name != user:
                continue
            if commit_datetime.date() != analysis_date:
                continue

            files_changed = len(commit.stats.files) if commit.stats.files else 0

            commits.append(
                Commit(
                    commit_hash=commit.hexsha,
                    author=commit.author.name,
                    message=commit.message.strip(),
                    date=commit_datetime,
                    files=files_changed,
                )
            )
        return commits
