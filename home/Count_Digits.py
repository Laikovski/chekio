"""
 You need to count the number of digits in a given string.

Input: A Str.
Output: An Int.
"""
def count_digits(text: str) -> int:
    # your code here
    count = 0
    for i in text:
        if i.isdigit():
            count += 1
    return count


if __name__ == '__main__':
    print("Example:")
    # print(count_digits('hi'))
    print(count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year'))