"""
 For the input of your function, you will be given one sentence. You have to return a corrected version,
 that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot),
then adding another one will be a mistake.

Input: A string.

Output: A string.
"""

def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """

    if text[-1] != ".":
        return text[0].upper() + text[1:] + "."
    else:
        return text[0].upper() + text[1:]




if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    print(correct_sentence("welcome to New York."))
    print(correct_sentence("hi"))