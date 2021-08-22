"""
Let's try some sorting. Here is an array with the specific rules.

The array (a list) has various numbers. You should sort it, but sort it by absolute value in ascending order.
For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20).
Your function should return the sorted list or tuple.

Precondition: The numbers in the array are unique by their absolute values.

Input: An array of numbers , a tuple..
Output: The list or tuple (but not a generator) sorted by absolute values in ascending order.
Addition: The results of your function will be shown as a list in the tests explanation panel.
"""

def checkio(values: list) -> list:
    # your code here
    return sorted(values, key= lambda x: abs(x))


if __name__ == '__main__':
    print("Example:")
    print(checkio([-20, -5, 10, 15]))