"""
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.
"""
from datetime import datetime
def date_time(time: str) -> str:
    months = {    1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'       }
    date,time = time.split()
    day,month,year = map(int,date.split('.'))
    hours,minutes = map(int,time.split(':'))
    hs = ''
    ms = ''
    if hours != 1:
        hs = 's'
    if minutes !=1:
        ms = 's'
    return f"{day} {months[month]} {year} year {hours} hour{hs} {minutes} minute{ms}"


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))