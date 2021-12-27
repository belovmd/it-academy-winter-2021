# ______________Example_1_Elementary___________________
# You have a positive integer. Try to find out how many digits it has?
# Input: A positive Int
# Output: An Int.


def number_length(a: int) -> int:
    # your code here
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
    # your code here
    if len(password) > 6:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert is_acceptable_password('short') == False
    # assert is_acceptable_password('muchlonger') == True
    # assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


# ______________Example_3_Elementary___________________
# You should return a given string in reverse order.
# Input: A string.
# Output: A string.


def backward_string(val: str) -> str:
    # your code
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
