"""
Example_1(Elementary)
You are given a sequence of strings.
You should join these strings into a chunk of text where the initial
strings are separated by commas.As a joke on the right handed robots,
you should replace all cases of the words "right" with the word "left",
even if it's a part of another word. All strings are given in lowercase.
Input: A sequence of strings.
Output: The text as a comma-separated string.
"""


def left_join(phrases: tuple) -> str:
    return ','.join(phrases).replace('right', 'left')


if __name__ == "__main__":
    print("Example:")
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        left_join(("left", "right", "left", "stop")) == "left,left,left,stop"), "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


"""
Example_2 (Elementary+)
In a given string you should reverse every word, but the words should stay in their places.
Input: A string.
Output: A string.
"""


def backward_string_by_word(text: str) -> str:
    return ' '.join(word[::-1] for word in text.split(' '))


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""
Example_3 (Elementary+)
You have a string that consist only of digits. You need to find how many zero digits
("0") are at the beginning
of the given string.
Input: A string, that consist of digits.
Output: An Int.
"""


def beginning_zeros(number: str) -> int:
    count = 0
    for i in range(len(number)):
        if number[i] == '0':
            count += 1
        else:
            break

    return count


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
