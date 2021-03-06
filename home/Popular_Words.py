"""
 In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.

When solving this task pay attention to the following points:

    The words should be sought in all registers. This means that if you need to find a word "one" then words like "one",
    "One", "oNe", "ONE" etc. will do.
    The search words are always indicated in the lowercase.
    If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.

Input: The text and the search words array.

Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring
in a given text.
"""

def popular_words(text: str, words: list) -> dict:
    # your code here
    text = text.lower()
    new_arr = text.split()
    new_dict = {}
    for i in new_arr:
        if i in words:
            if i in new_dict.keys():
                new_dict[i] +=  1
            else:
                new_dict[i] = 1

    for i in words:
        if not i in new_dict.keys():
            new_dict[i] = 0
    return new_dict


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))