# 1
# Учитывая случайное неотрицательное число, вы должны вернуть
# цифры этого числа в массиве в обратном порядке.
# Example
# 348597 => [7,9,5,8,4,3]

n = input('Введите число: ')
lst = []
lst.extend(n)
print(lst[::-1])

# 2
# Ваша цель - удалить первый и последний символы строки.
# Вам дается один параметр - исходная строка.
# Вам не нужно беспокоиться о строках, содержащих менее двух символов.

str_ = input('Введите строку: ')
str_new = str_[1:-1]
print(str_new)

# 3
# Ваша задача - вернуть сумму следующего ряда до n-го члена (параметра).
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

n = int(input('Введите число: '))
sum_ = 1
for element in range(1, n):
    sum_ += 1 / (element + 3)
print(round(sum_, 2))

# 4
# Введите 2 строки s1 и s2, содержащие только буквы от a до z.
# Необходимо вернуть новую отсортированную по алфавиту строку,
# содержащую буквы исходных строк s1 и s2 -
# каждая взятая только один раз, т.е. буквы не должны повторяться.

s1 = input('Введите строку s1: ')
s2 = input('Введите строку s2: ')
lst = []
for element in s1:
    if element not in lst:
        lst.extend(element)
for element in s2:
    if element not in lst:
        lst.extend(element)
lst.sort()
print(''.join(lst))

# 5
# Даны 2 целых числа a и b, которые могут быть положительными или отрицательными,
# найти сумму всех целых чисел между ними включительно и вернуть ее.
# Если два числа равны, верните a или b.

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
sum_ = a + b
if a <= b:
    step = 1
elif a > b:
    step = -1
for element in range(a, b, step):
    sum_ += element
sum_ -= a
print(sum_)

# 6
# In a given string you should reverse every word, but the words
# should stay in their places.
# Precondition: The line consists only from alphabetical symbols and spaces.
# Examples:
# backward_string_by_word('') == ''
# backward_string_by_word('world') == 'dlrow'
# backward_string_by_word('hello world') == 'olleh dlrow'
# backward_string_by_word('hello   world') == 'olleh   dlrow'
# backward_string_by_word('welcome to a game') == 'emoclew ot a emag'

def backward_string_by_word(text):
    lst = []
    lst.extend(text)
    lst.extend(' ')
    result = []
    str_ = ''
    for i in range(len(lst)):
        if lst[i].isalpha():
            str_ += lst[i]
        else:
            result.append(str_[::-1])
            result.append(lst[i])
            str_ = ''
    return ''.join(result)[:-1]

print(backward_string_by_word(''))

# 7
# You are given a list of files. You need to sort this list by
# the file extension. The files with the same extension should
# be sorted by name.
#
# Some possible cases:
#
# Filename cannot be an empty string;
# Files without the extension should go before the files with one;
# Filename ".config" has an empty extension and a name ".config";
# Filename "config." has an empty extension and a name "config.";
# Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
# Filename ".imp.xls" has an extension "xls" and a name ".imp".

def sort_ext(tpl):
    return (tpl[1][1:], tpl[0])

def sort_by_ext(files):
    list_new = []
    for file in files:
        x = file.rfind('.')
        if not x:
            name = file
            ext = ''
        else:
            name = file[:x]
            ext = file[x:]
        list_new.append((name, ext))
    list_new.sort(key=sort_ext)
    result = [''.join(tpl_) for tpl_ in list_new]
    return result

print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']))
