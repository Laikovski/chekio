"""
 Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times
 they appear in elements. If two elements have the same frequency, they should end up in the same order as the first
 appearance in the iterable.

Input: Iterable
Output: Iterable

Precondition: elements can be ints or strings

The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of Continuing
Education by Ilkka Kokkarinen
"""
from collections import Counter

def frequency_sort(items):
    # your code here

    new = [item for items, c in Counter(items).most_common()
                                      for item in [items] * c]



    return new

if __name__ == '__main__':
    print("Example:")
    print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))
    print(list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])))