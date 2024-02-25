from collections import defaultdict
from datetime import datetime, timedelta
from typing import List, Dict, Union


def get_birthdays_per_week(users: List[Dict[str, Union[str, datetime]]]):
    results = defaultdict(list)
    today = datetime.today().date() + timedelta(days=1)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            if (dow := birthday_this_year.weekday()) >= 5:
                birthday_this_year = birthday_this_year + timedelta(days=(0 - dow + 7) % 7)

            results[birthday_this_year.strftime('%A')].append(name)

    [print(f'{dow}: ' + ', '.join(names)) for dow, names in results.items()]
