"""
You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you
see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
"""
from datetime import datetime


def time_converter(time):
    d = datetime.strptime(time, "%H:%M")
    res = d.strftime("%I:%M %p")

    if 'AM' in res:
        res = res.replace('AM', 'a.m.')
    elif 'PM' in res:
        res = res.replace('PM', 'p.m.')

    if res[0] == '0':
        res = res[0].replace('0', '') + res[1:]
    return res


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))
    print(time_converter('09:00'))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert time_converter('12:30') == '12:30 p.m.'
    # assert time_converter('09:00') == '9:00 a.m.'
    # assert time_converter('23:15') == '11:15 p.m.'
    # print("Coding complete? Click 'Check' to earn cool rewards!")