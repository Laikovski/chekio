"""
 You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the
  given string.

Input: A string, that consist of digits.
Output: An Int.
"""

def beginning_zeros(number: str) -> int:
    # your code here
    return len(number) - len(number.lstrip('0'))



if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('00100'))