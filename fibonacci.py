# -*- coding: utf-8 -*-

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after nn months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
# http://rosalind.info/problems/fib/

def fib(n, k):
    a, b = 1, 1
    for i in range(2, int(n)):
        # 只需要保存最近两个月的数量即可
        a, b = b, int(k)  *a + b
    print(b)
fib(5, 3)
