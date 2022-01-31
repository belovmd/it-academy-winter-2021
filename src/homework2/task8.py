# 8. Зарегистрируйтесь на одном (или нескольких) из сайтов:
# https://py.checkio.org/ , https://www.codewars.com, https://www.hackerrank.com/, https://acmp.ru
# И решите 1-5 задач уровня Elementary и advanced.
# Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.

# codewars.com, elementary #1
# Remove all of the vowels from string
# Note: for this kata "y" isn't considered a vowel.
def disemvowel(string_):
    for elem in string_:
        if elem in "aoeuiAOEUI":
            str_ = string_.replace(elem, "")
            string_ = str_
    return string_


