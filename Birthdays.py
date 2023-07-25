from datetime import datetime, timedelta

users=[{'name': 'Вася', 'birthday': datetime(year=2023, month=7, day=7)},
       {'name': 'Петя', 'birthday': datetime(year=2023, month=7, day=27)},
       {'name': 'Коля', 'birthday': datetime(year=2023, month=7, day=28)},
       {'name': 'Юля', 'birthday': datetime(year=2023, month=2, day=7)},
       {'name': 'Настя', 'birthday': datetime(year=2023, month=7, day=23)},
       {'name': 'Олег', 'birthday': datetime(year=2023, month=7, day=28)}]


def get_birthdays_per_week(users: list) -> None:
    """Функція для виведення іменинників для їхнього привітання"""
    to_day = datetime.now().date()
    datetofriday = timedelta(days=5)
    previous_week = to_day - timedelta(weeks=1)
    previous_saturday = previous_week + timedelta(days=5 - previous_week.weekday())
    day_of_week = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця', 'Субота попереднього тижня', 'Неділя попереднього тижня']
    happy_birthday = {}
    for user in users:
        birthday = user['birthday'].date()
        week_day = birthday.weekday()
        if previous_saturday <= birthday <= (to_day + datetofriday):
            day = day_of_week[week_day]
            if day in happy_birthday:
                happy_birthday[day].append(user['name'])
            else:
                happy_birthday[day] = [user['name']]

    birthdays_str = '\n'.join([f"{day}: {', '.join(names)}" for day, names in happy_birthday.items()])
    print(birthdays_str)



if __name__=='__main__':
    get_birthdays_per_week(users)








