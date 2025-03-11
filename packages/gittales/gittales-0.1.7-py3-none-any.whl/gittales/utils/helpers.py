from datetime import datetime, date, time

def parse_date(date_str: str) -> date:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

def calculate_duration(start: datetime, end: datetime) -> float:
    return (end - start).total_seconds() / 60
