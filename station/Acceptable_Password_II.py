"""
 In this mission you need to create a password verification function.

Those are the verification conditions:

    the length should be bigger than 6;
    should contain at least one digit.

Input: A string.

Output: A bool.
"""
import re
def is_acceptable_password(password: str) -> bool:
    if len(password) > 6 and any(map(str.isdigit, password)) and any(letter.isalpha() for letter in password):
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('dddsdd'))
    print(is_acceptable_password("1234567h"))