"""
 In a given text you need to sum the numbers while excluding any digits that form part of a word.

The text consists of numbers, spaces and letters from the English alphabet.

Input: A string.

Output: An int.
"""

def sum_numbers(text: str) -> int:
    new = list(text.split(' '))
    res = 0
    for i in new:
        try:
            res += int(i)
        except:
            continue
    return res



if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))
    print(sum_numbers('who is 1st here'))
    print(sum_numbers('5 plus 6 is'))