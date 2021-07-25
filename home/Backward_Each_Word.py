"""
 In a given string you should reverse every word, but the words should stay in their places.

Input: A string.
Output: A string.
"""

def backward_string_by_word(text: str) -> str:
    new_list = list(text.split(' '))
    res = ''
    for i in new_list:
        if len(text) == 0:
            return text

        else:
            if i == '':
                res += ' '
            else:
                res += i[::-1] + ' '

    return res.rstrip(' ')
if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))
    print(backward_string_by_word('welcome to a game'))
    print(backward_string_by_word('hello   world'))
    print(backward_string_by_word('world'))