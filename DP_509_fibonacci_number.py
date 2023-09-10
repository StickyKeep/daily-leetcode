"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
https://leetcode.com/problems/fibonacci-number/description/?envType=study-plan-v2&envId=dynamic-programming
"""

# First solution: 

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        tab = [0] * (n + 1)
        tab[1] = 1

        for i in range(2, n + 1):
            tab[i] = tab[i - 1] + tab[i - 2]

        return tab[n]

# Runtime 32ms
# Beats 94.71%of users with Python3
# Memory 16.27MB
# Beats 61.49%of users with Python3