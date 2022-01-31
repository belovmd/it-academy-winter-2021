# Additional task
# 1. Create a function that takes a Roman numeral as its argument and returns its value
# as a numeric decimal integer. You don't need to validate the form of the Roman numeral.
# Modern Roman numerals are written by expressing each decimal digit of the number to be
# encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is
# rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII"
# (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter
# in descending order.

def solution(roman):
    dict_symb = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0
    for elem in range(len(roman)):
        if elem == len(roman) - 1:
            val += dict_symb[roman[elem]]
            return val
        if dict_symb[roman[elem]] < dict_symb[roman[elem + 1]]:
            val -= dict_symb[roman[elem]]
        else:
            val += dict_symb[roman[elem]]
    return val

# 2. You are given an array (which will have a length of at least 3, but could be very large)
# containing integers. The array is either entirely comprised of odd integers or entirely
# comprised of even integers except for a single integer N. Write a method that takes the
# array as an argument and returns this "outlier" N.

    def find_outlier(integers):
        odd = []
        even = []
        for numb in integers:
            if numb % 2 == 0:
                even.append(numb)
            else:
                odd.append(numb)
        if len(odd) > len(even):
            return even[0]
        else:
            return odd[0]
