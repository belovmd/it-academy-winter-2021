def first_word(text: str) -> str:
    return text.split(' ', 1)[1]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))


def number_length(number: int) -> int:
    return len(str(number))


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))


def is_all_upper(text: str) -> bool:
    if text.upper() == text:
        return True
    elif len(text) == 0:
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))


def max_digit(number: int) -> int:
    m = 0
    for n in str(number):
        if int(n) > m:
            m = int(n)
    return m


if __name__ == '__main__':
    print("Example:")
    print(max_digit(35))


n = int(input())
if n >= 1 and n <= 100:
    if n % 2 != 0:
        print("Weird")
    else:
        if n in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")
