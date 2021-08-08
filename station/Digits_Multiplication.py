"""
We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission.
In order to see all other solutions you should change the filter.

You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.
"""

def checkio(number: int) -> int:

    res = 1
    for i in str(number).replace('0', ''):
        res *= int(i)

    return res

if __name__ == '__main__':
    print('Example:')
    print(checkio(123405)) # 120
    print(checkio(999)) # 729
    print(checkio(1111)) # 1
    print(checkio(1000)) # 1