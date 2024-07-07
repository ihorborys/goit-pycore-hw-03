from datetime import date, datetime
"""Transforms date string to date object
Throws:
    ValueError, TypeError when date format is not: %Y-%m-%d
"""
def transform_string_to_date(date: str) -> date:
    try:
        return datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        print("Please, enter data in format: 'YYYY-MM-DD'")

"""Calculates distance between dates"""
def get_days_from_today(date_one: date, date_two: date) -> int:
    try:
        return (date_two - date_one).days
    except (ValueError, TypeError):
        print("Please, enter data in format: 'YYYY-MM-DD'")

date_one = transform_string_to_date("1988-10-30")
date_two = datetime.today().date()

print(get_days_from_today(date_one, date_two))
