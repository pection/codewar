# he purpose of this kata is to write a program that can do some algebra.
# Write a function expand that takes in an expression with a single, one character variable,
# and expands it. The expression is in the form (ax+b)^n where a and b are integers which may
# be positive or negative, x is any single character variable, and n is a natural number.
# If a = 1, no coefficient will be placed in front of the variable. If a = -1, a "-" will e placed in front of the variable.#
# The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e
# are the coefficients of the term, x is the original one character variable that was passed in
# the original expression and b, d, and f, are the powers that x is being raised to in each term and are in decreasing order.
# If the coefficient of a term is zero, the term should not be included. If the coefficient of a term is one,
# the coefficient should not be included. If the coefficient of a term is -1, only the "-" should be included.
# If the power of the term is 0, only the coefficient should be included. If the power of the term is 1,
# the caret and power should be excluded.
import math
# import sympy
# def expand(expr):

#!C:/Python34/python.exe

import sys, re
from math import pow

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def pascal(row, num):
    return nCr(row, num - 1)

def pascal_for_row(row):
    row_nums = list()
    for i in range(1, row + 2):
        row_nums.append(pascal(row, i))

    return row_nums


BINOMIAL_REGEX = "\\((?:(\\d+)([a-zA-Z])(?:\\^(\\d+)?)?)(\\+|\\-)(?:(\\d+)([a-zA-Z])(?:\\^(\\d+)?)?)\\)(?:\\^(\\d+))"

binomial = input("Enter a binomial to expand: ").replace(" ", "")
match = re.search(BINOMIAL_REGEX, binomial)

if match is None:
    print("Invalid Binomial.")
    sys.exit(0)

first_coeff = int(match.group(1))
first_var = match.group(2)
first_exp = int(match.group(3) if match.group(3) else 1)

add = match.group(4) == '+'

second_coeff = int(match.group(5))
second_var = match.group(6)
second_exp = int(match.group(7) if match.group(7) else 1)

power = int(match.group(8))

pascal_row = pascal_for_row(power)
expanded = ""

for i in range(0, len(pascal_row)):
    if i is len(pascal_row) - 1:
        expanded += str(int(pow(second_coeff, i)) * pascal_row[i]) + str(second_var) + "^" + str(i) + " "
    elif i is 0:
        expanded += str(int(pow(first_coeff, power - i)) * pascal_row[i]) + str(first_var) + "^" + str(power - i) + " "
    else:
        expanded += str(int(pow(first_coeff, power - i)) * int(pow(second_coeff, i)) * pascal_row[i]) + str(first_var)
        if power - i is not 1:
            expanded += "^" + str(power - i) + "*"

        expanded += str(second_var) + " "
        if i is not 1:
            expanded += "^" + str(i) + " "

        if i is not len(pascal_row) - 1:
            expanded += ("+ " if add else "- ")

print(expanded)


# test.assert_equals(expand("(x+1)^0"), "1")
# test.assert_equals(expand("(x+1)^1"), "x+1")
# test.assert_equals(expand("(x+1)^2"), "x^2+2x+1")
#
# test.assert_equals(expand("(x-1)^0"), "1")
# test.assert_equals(expand("(x-1)^1"), "x-1")
# test.assert_equals(expand("(x-1)^2"), "x^2-2x+1")
#
# test.assert_equals(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
# test.assert_equals(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
# test.assert_equals(expand("(7x-7)^0"), "1")
