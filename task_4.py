from typing import List, Dict
from datetime import datetime

users_list = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.05.13"},
    {"name": "Ian Wright", "birthday": "1978.10.27"},
    {"name": "Tomas Schmidt", "birthday": "1978.07.13"},
    {"name": "Scott White", "birthday": "1978.07.14"}
]


def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    today = datetime.today().date()
    bd_data_list = []

    for user in users:
        user_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if user_date.month == today.month and today.day <= user_date.day <= today.day + 7:
            day = user_date.day
            c_date = datetime(today.year, today.month, day)
            if c_date.weekday() == 5:
                day += 2
            if c_date.weekday() == 6:
                day += 1

            user_bd_data = {
                "name": user["name"],
                "congratulation_date": f"{today.year}.{today.month}.{day}"
            }
            bd_data_list.append(user_bd_data)
        bd_data_list.sort(key=get_day)

    print(bd_data_list)
    return bd_data_list


def get_day(element):
    return datetime.strptime(element["congratulation_date"], "%Y.%m.%d").date().day


get_upcoming_birthdays(users_list)