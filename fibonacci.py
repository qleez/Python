# -*- coding: utf-8 -*-

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after nn months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
# http://rosalind.info/problems/fib/

'''
Month 0: 1 pair exists (young)
Month 1: 1 pair exists (adult)
Month 2: 1 pair exists (adult) + k pairs exist (young) = 1 + k total
Month 3: 1 + k pairs exist (adult) + k pairs exist (young) = 1 + 2k total
Month 4: 1 + 2k pairs exist (adult) + k (1 + k) pairs exist (young) = 1 + k(3 + k) total
Month 5: 1 + 3k + k^2 pairs exist (adult) + k (1 + 2k) pairs exist (young) = 1 + k(4 + 3k) total
and so on...

Notice that with each month, the total number of rabbit pairs is k * number of adults (which are two generations old) + number of young pairs (which are 1 generation old). Therefore the amount of rabbits at generation n is k * number of rabbits at generation n - 2 (as these are now all adults) + number of rabbits at generation n - 1

Mathematically: f(0) = 1, f(1) = 1, f(n) = f(n-1) + k * f(n-2).
'''

def fib(n, k):
    if n == 1 or n == 2:
        return 1
    else: 
        return (fib(n-1, k) + k * fib(n-2, k))
print(fib(5, 3))
