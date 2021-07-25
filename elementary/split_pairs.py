"""
 Split the string into pairs of two characters. If the string contains an odd number of characters,
 then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.
Output: An iterable of strings.

Precondition: 0<=len(str)<=100
"""

def split_pairs(a):
    # your code here
    if len(a) % 2 != 0:
        a = f'{a}_'

    return [a[i:i+2] for i in range(0, len(a), 2)]

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcde')))
    print(list(split_pairs('abcd')))