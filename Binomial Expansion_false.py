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
def expand(expr):


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
