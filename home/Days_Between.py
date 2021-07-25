"""
 How old are you in a number of days? It's easy to calculate - just subtract your birthday from today.
 We could make this a real challenge though and count the difference between any dates.

You are given two dates as an array with three numbers - a year, month and day.
For example: 19 April 1982 will be (1982, 4, 19). You should find the difference in days between the given dates.
For example between today and tomorrow = 1 day. The difference will always be either a positive number or zero, so
don't forget about the absolute value.

Input: Two dates as tuples of integers.

Output: The difference between the dates in days as an integer.

Precondition: Dates between 1 january 1 and 31 december 9999. Dates are correct.
"""
from datetime import date, timedelta
def days_diff(a, b):
    # your code here
    start = date(year = a[0], month = a[1], day = a[2])
    finish = date(year = b[0], month = b[1], day = b[2])
    res = abs(start - finish)

    return res.days


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))
    print(days_diff((2014, 1, 1), (2014, 8, 27)))
    print(days_diff((2014, 8, 27), (2014, 1, 1)))
    print(days_diff([1,1,1],[9999,12,31]))