# ______________Example_1_Elementary___________________
# You have a positive integer. Try to find out how many digits it has?
# Input: A positive Int
# Output: An Int.


def number_length(a: int) -> int:
    a = str(a)
    str_ = len(a)
    return str_


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")


# ______________Example_2_Elementary___________________
# You need to create a password verification function.
# The verification condition is:
# the length should be bigger than 6.
# Input: A string.
# Output: A bool.


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False


true = True
false = False
if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == false
    assert is_acceptable_password('muchlonger') == true
    assert is_acceptable_password('ashort') == false
    print("Coding complete? Click 'Check' to earn cool rewards!")


# ______________Example_3_Elementary___________________
# You should return a given string in reverse order.
# Input: A string.
# Output: A string.


def backward_string(val: str) -> str:
    return val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")


# ______________Example_4_Simple________________________
# You have to split a given array into two arrays.
# If it has an odd amount of elements, then the first array should have more elements.
# If it has no elements, then two empty arrays should be returned.
# Input: Array.
# Output: Array or two arrays.


def split_list(items: list) -> list:
    len_items = (len(items) + 1) // 2
    return [items[: len_items], items[len_items:]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")


# ______________Example_5_Moderate_________________________
# You are given an expression with numbers, brackets and operators.
# For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]".
# Brackets are used to determine scope or to restrict some expression.
# If a bracket is open, then it must be closed with a closing bracket of the same type.
# The scope of a bracket must not intersected by another bracket.
# In this task you should make a decision,
# whether to correct an expression or not based on the brackets.
# Do not worry about operators and operands.
#
# Input: An expression with different of types brackets as a string (unicode).
#
# Output: A verdict on the correctness of the expression in boolean (True or False).


def checkio(expression):
    my_list = list()
    my_dict = {'(': ')', '[': ']', '{': '}'}
    for elem in expression:
        if elem in my_dict.keys():
            my_list.append(elem)
        elif elem in my_dict.values():
            if my_list and elem == my_dict[my_list[-1]]:
                my_list.pop()
            else:
                return False
    return not my_list


true = True
false = False
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == true, "Simple"
    assert checkio("{[(3+1)+2]+}") == true, "Different types"
    assert checkio("(3+{1-1)}") == false, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == true, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == false, "One is redundant"
    assert checkio("2+3") is True, "No brackets, no problem"
