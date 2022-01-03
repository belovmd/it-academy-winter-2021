import re

str_ = input('input string')
str_ = re.sub(r'[^\w\s]', ' ', str_)
str_ = str_.split()
max_string = max(str_, key=len)
print(max_string)
