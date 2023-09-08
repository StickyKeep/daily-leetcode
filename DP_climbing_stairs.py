"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=dynamic-programming
"""

# Memoization

class Solution:
    def climbStairs(self, n: int) -> int:
        def stairbonacci(n, stair_dict={}):
            if n in stair_dict:
                return stair_dict[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            stair_dict[n] = stairbonacci(n-1, stair_dict) + stairbonacci(n-2, stair_dict)
            return stair_dict[n]
        return stairbonacci(n)
    
# Runtime 30ms
# Beats 95.09% of users with Python3    

### ------

# Tabular

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: 
            return 0
        elif n == 1: 
            return 1
        elif n == 2:
            return 2
        else:
            stairlist = [0] * (n)
            stairlist[0] = 1
            stairlist[1] = 2
            for i in range(2,n):
                stairlist[i] = (stairlist[i-1] + stairlist[i-2])
            return stairlist[n-1]


# Runtime 39ms
# Beats 59.62% of users with Python3

# Memory 16.37MB
# Beats 27.12%of users with Python3