# Not all of the elements are important. What you need to do here is to remove from the
# list all of the elements before the given one. For the illustration we have a
# list [1, 2, 3, 4, 5] and we need to remove all elements that go before 3 - which is 1
# and 2. We have two edge cases here: (1) if a cutting element cannot be found, then the
# list shoudn't be changed. (2) if the list is empty, then it should remain empty.
# Input: List and the border element.
# Output: Iterable (tuple, list, iterator ...).
# Example:
# remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
# remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]


from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        result = items[items.index(border)::]
    else:
        result = items
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7,
                                                                       7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")


# Split the string into pairs of two characters. If the string contains an odd number of
# characters, then the missing second character of the final pair should be replaced with
# an underscore ('_').
# Input: A string.#
# Output: An iterable of strings.#
# Example:#
# split_pairs('abcd') == ['ab', 'cd']
# split_pairs('abc') == ['ab', 'c_']


def split_pairs(a):
    result = []
    count = len(a)
    a = list(a)
    if not a:
        return result
    else:
        while count:
            if count >= 2:
                result.append(a[0] + a[1])
                a.pop(0)
                a.pop(0)
                count -= 2
            else:
                result.append(a[0] + '_')
                a.pop(0)
                count -= 1
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")


# Check if a given string has all symbols in upper case. If the string is empty or doesn't
# have any letter in it - function should return True.
# Input: A string.
# Output: a boolean.
# Example:
# is_all_upper('ALL UPPER') == True
# is_all_upper('all lower') == False
# is_all_upper('mixed UPPER and lower') == False
# is_all_upper('') == True
# is_all_upper('444') == True
# is_all_upper('55 55 5') == True
# Precondition: a-z, A-Z, 1-9 and spaces


def is_all_upper(text: str) -> bool:
    result = True
    if not text:
        result = True
    else:
        for ch in text:
            if 'A' <= ch <= 'Z' or '0' <= ch <= '9' or ch == " ":
                result = True
            else:
                result = False
    return result


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') is True
    assert is_all_upper('all lower') is False
    assert is_all_upper('mixed UPPER and lower') is False
    assert is_all_upper('') is True
    assert is_all_upper('     ') is True
    assert is_all_upper('444') is True
    assert is_all_upper('55 55 5') is True
    assert is_all_upper('Hi') is False
    print("Coding complete? Click 'Check' to earn cool rewards!")


# You have a string that consist only of digits. You need to find how many zero digits
# ("0") are at the beginning of the given string.
# Input: A string, that consist of digits.
# Output: An Int.
# Example:
# beginning_zeros('100') == 0
# beginning_zeros('001') == 2
# beginning_zeros('100100') == 0
# beginning_zeros('001001') == 2
# beginning_zeros('012345679') == 1
# beginning_zeros('0000') == 4


def beginning_zeros(number: str) -> int:
    count = 0
    for char in number:
        if char == '0':
            count += 1
        else:
            return count
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


# Find the nearest value to the given one.
# You are given a list of values as set form and a value for which you need to find
# the nearest one.
# For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17, and we need
# to find the nearest value to the number 9. If we sort this set in the ascending order,
# then to the left of number 9 will be number 7 and to the right - will be number 10.
# But 10 is closer than 7, which means that the correct answer is 10.
# A few clarifications:
# If 2 numbers are at the same distance, you need to choose the smallest one;
# The set of numbers is always non-empty, i.e. the size is >=1;
# The given value can be in this set, which means that it’s the answer;
# The set can contain both positive and negative numbers, but they are always integers;
# The set isn’t sorted and consists of unique numbers.
# Input: Two arguments. A list of values in the set form. The sought value is an int.
# Output: Int.


def nearest_value(values: set, one: int) -> int:
    if one not in values:
        min_v = max_v = one
        while min_v or max_v not in values:
            min_v -= 1
            max_v += 1
            if min_v in values:
                return min_v
            elif max_v in values:
                return max_v
    else:
        return one


if __name__ == "__main__":
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
