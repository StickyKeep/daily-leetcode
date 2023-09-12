""" Easy:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
https://leetcode.com/problems/contains-duplicate/description/
"""

# Second sub

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# First sub

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        