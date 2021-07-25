"""
 You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...).
 Then multiply this summed number and the final element of the array together. Don't forget that the first element
 has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.
Output: The number as an integer.

Precondition: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
"""

def checkio(array: list) -> int:
    res = 0
    if len(array) == 0:
        return 0
    for i in range(0, len(array), 2):
        res += array[i]

    return res * array[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    print(checkio([1, 3, 5]))
    print(checkio([]))