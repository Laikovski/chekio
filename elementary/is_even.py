"""
 Check if the given number is even or not. Your function should return True if the number is even, and False if the
 number is odd.

Input: An int.
Output: A bool.

Precondition: both given ints should be between -1000 and 1000
"""

def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))
    print(is_even(0))
    print(is_even(5))