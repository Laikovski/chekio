"""
 In a given word you need to check if one symbol goes only right after another.

Cases you should expect while solving this challenge:

    If more than one symbol is in the list you should always count the first one
    one of the symbols are not in the given word - your function should return False;
    any symbol appears in a word more than once - use only the first one;
    two symbols are the same - your function should return False;
    the condition is case sensitive, which means 'a' and 'A' are two different symbols.

Input: Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a
symbold that should go after the first one.
"""

def goes_after(word: str, first: str, second: str) -> bool:
    return 0 < word.find(second) == word.find(first) + 1


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'k'))
    print(goes_after("almaz","m","a"))