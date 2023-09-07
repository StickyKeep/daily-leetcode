"""
1. Two Sum, Easy: https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. 
"""

#Final solution:

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_numbers = {}
        for index, value in enumerate(nums):
            sum = target - value
            if sum in dict_numbers:
                return [dict_numbers[sum], index]
            dict_numbers[value] = index
        
# Runtime: 57ms
# Beats 94.54% of users with Python3

# Memory 17.66MB
# Beats 33.35% of users with Python3

# First solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value in enumerate(nums):
            for n, value2 in enumerate(nums):
                if value + value2  == target and i != n:
                    return i, n
                

# Runtime: 4412ms
# Beats 8.18%of users with Python3

# Memory: 17.08MB
# Beats 90.80%of users with Python3

