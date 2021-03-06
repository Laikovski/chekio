"""
 You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

    There can be dots and commas in a string.
    A string can start with a letter or, for example, a dot or space.
    A word can contain an apostrophe and it's a part of a word.
    The whole text can be represented with one word and that's it.

Input: A string.

Output: A string.
"""

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    text = text.lstrip(' ')
    if ' ' in text:
        text = text.split(' ')
        if '.' in text[0]:
            return text[1]
        else:
            return text[0].rstrip(',')
    else:
        text = text.split('.')
        return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("greetings, friends"))
    print(first_word(" a word "))
    # print(first_word("Hello world"))
    # print(first_word("... and so on ..."))
    # print(first_word("Hello.World"))