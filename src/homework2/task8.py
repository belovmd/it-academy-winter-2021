# Открытая задача:
# 8. Зарегистрируйтесь на одном (или нескольких) из сайтов:
# https://py.checkio.org/ , https://www.codewars.com,   https://www.hackerrank.com/,
# https://acmp.ru И решите 1-5 задач уровня Elementary и advanced.
# Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.

# 1. Try to find out how many zeros a given number has at the end.
# Input: A positive Int
# Output: An Int.

def end_zeros(num: int) -> int:
    return len(str(num)) - len(str(num).rstrip('0'))

# 2. Check if a given string has all symbols in upper case.
# If the string is empty or doesn't have any letter in it - function should return True.
# Input: A string.
# Output: a boolean.

    def is_all_upper(text: str) -> bool:
        if text.upper() == text or len(text) == 0:
            return True
        return False

# 3. You are given a non-empty list of integers (X). For this task, you should
# return a list consisting of only the non-unique elements in this list.
# To do so you will need to remove all unique elements
# (elements which are contained in a given list only once).
# When solving this task, do not change the order of the list.
# Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
# Input: A list of integers.
# Output: An iterable of integers.

        def checkio(data: list) -> list:
            new_list = []
            for i in list(data):
                if data.count(i) > 1:
                    new_list.append(i)
            return new_list

# 4. Split the string into pairs of two characters. If the string contains an odd
# number of characters, then the missing second character of the final pair should
# be replaced with an underscore ('_').
            def split_pairs(a):
                new_list_ = []
                for i in range(0, len(a), 2):
                    element = a[i:i + 2]
                    if len(element) == 1:
                        new_list_.append(element + '_')
                    else:
                        new_list_.append(element)
                return new_list_

# 5. Every true traveler must know how to do 3 things: fix the fire,
# find the water and extract useful information from the nature around him.
# Programming won't help you with the fire and water, but when
# it comes to the information extraction - it might be just the thing you need.
# Your task is to find the angle of the sun above the horizon knowing
# the time of the day. Input data: the sun rises in the East at 6:00 AM,
# which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its
# zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of the
# sunset so the angle is 180 degrees. If the input will be the time of the night
# (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".

                from typing import Union

                def sun_angle(time: str) -> Union[int, str]:
                    angle_in_minute = 90 / (6 * 60)
                    h, m = map(int, time.split(':'))
                    if 600 <= int(time.replace(':', '')) <= 1800:
                        minute = (h - 6) * 60 + m
                        return angle_in_minute * minute
                    return 'I don\'t see the sun!'
