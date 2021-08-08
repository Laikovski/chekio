""" You have a text and a list of words. You need to check if the words in a list appear in the same order as in
the given text.

Cases you should expect while solving this challenge:

    a word from the list is not in the text - your function should return False;
    any word can appear more than once in a text - use only the first one;
    two words in the given list are the same - your function should return False;
    the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
    the text includes only English letters and spaces.

Input: Two arguments. The first one is a given text, the second is a list of words.

Output: A bool. """

def words_order(text, words):
    arr = text.split()
    index = -1
    for i in words:
        if i in arr and arr.index(i) > index:
            index = arr.index(i)
        else:
            return False

    return True

if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))
    print(words_order('hi world im here', ['here', 'world']))
    print(words_order('hi world im here', ['world', 'world']))
    print(words_order('hi world im here', ['world', 'here', 'hi']))
    print(words_order('', ['world', 'here']))