"""
Easy. You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=dynamic-programming
"""

# First solution:

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost or len(cost) < 2:
            return 0
            
        dp_cost = [0] * len(cost)

        dp_cost[0] = cost[0]
        dp_cost[1] = cost[1]

        for i in range(2, len(cost)):
            dp_cost[i] = cost[i] + min(dp_cost[i-1], dp_cost[i-2])
            
        return min(dp_cost[-1], dp_cost[-2])
        

# Runtime 64ms
# Beats 51.51% of users with Python3
# Memory 16.26MB
# Beats 98.87% of users with Python3