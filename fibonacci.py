# -*- coding: utf-8 -*-

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after nn months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
# http://rosalind.info/problems/fib/

def fib(n, k):
    if n < 0:
         print("n must be a positive value")
    if n is 0 or n is 1:
        return 1
    else: 
        return (fib(n-1, k) + k * fib(n-2, k))
fib(5, 3)
