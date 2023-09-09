"""
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=dynamic-programming
"""

# First solution with modified code from 509. Fibonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        tab = [0] * (n + 1)
        tab[1] = 1
        tab[2] = 1

        for i in range(3, n + 1):
            tab[i] = tab[i - 1] + tab[i - 2] + tab[i - 3]

        return tab[n]

        
# Runtime 44ms
# Beats 31.00%of users with Python3
# Memory 16.16MB
# Beats 90.48%of users with Python3