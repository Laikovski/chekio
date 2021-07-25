"""
 Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession . For example, the string "start 5 one two three 7
end" contains three words in succession.

Input: A string with words.
Output: The answer as a boolean.

Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
0 < len(words) < 100
"""

def checkio(words: str) -> bool:
    new_list = list(words.split(' '))

    count = 0
    for word in new_list:
        if word.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    print(checkio("He is 123 man"))
    print(checkio("Hi"))
    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12 "))

