# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/
# difficulty: easy

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in sum_map:
                return [sum_map[diff], i]
            sum_map[n] = i