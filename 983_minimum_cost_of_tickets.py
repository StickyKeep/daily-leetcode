""" Medium:
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.
https://leetcode.com/problems/minimum-cost-for-tickets/description/?envType=study-plan-v2&envId=dynamic-programming
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in day_set:
                dp[day] = dp[day - 1]
                continue

            cost1 = dp[day - 1] + costs[0]
            cost7 = dp[day - 7] + costs[1] if day - 7 >= 0 else 0 + costs[1] # Don't wanna break time
            cost30 = dp[day - 30] + costs[2] if day - 30 >= 0 else 0 + costs[2]

            dp[day] = min(cost1, cost7, cost30)

        return dp[-1]

# Runtime 36ms
# Beats 98.75% of users with Python3
# Memory 16.24MB
# Beats 91.06% of users with Python3