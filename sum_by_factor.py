# Given an array of positive or negative integers

# I= [i1,..,in]

# you have to produce a sorted array P of the form

# [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

# P will be sorted by increasing order of the prime numbers. The final result 
# has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

# Example:

# I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
# [2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

# Notes:

# It can happen that a sum is 0 if some numbers are negative!
# Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, 
# the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

# In Fortran - as in any other language - the returned string is not permitted to contain 
# any redundant trailing whitespace: you can use dynamically allocated character strings.


from collections import defaultdict
def sum_for_list(lst):

    def factors(x):
        p_facs = []
        i = 2
        while x > 1 or x < -1:
            if x % i == 0:
                p_facs.append(i)
                x //= i
            else:
                i += 1
        return list(set(p_facs))
    
    fac_dict = defaultdict(int)
    
    for i in lst:
        for fac in factors(i):
            fac_dict[fac] += i
            
    return sorted([[k,v] for k,v in fac_dict.items()])



import subprocess
from itertools import chain

def prime_factors (n):
    out = subprocess.run(["factor", str(n)], stdout=subprocess.PIPE)
    out = str(out).split(':')[1].split('\\n')[0].split()
    return [int(s) for s in out]

def sum_for_list(L):
    P  = list(chain(prime_factors(abs(n)) for n in L))
    zP = list(zip(L, P))
    sP = sorted(set(p for l in P for p in l))
    return [[p, sum(e[0] for e in zP if p in e[1])] for p in sP]

a = [12, 15]	
test.assert_equals(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])

a = [15, 21, 24, 30, 45]
test.assert_equals(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])