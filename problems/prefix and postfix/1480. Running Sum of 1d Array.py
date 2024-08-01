# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/description
# difficulty: easy

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = 0
        sum_nums = []
        for num in nums:
            running_sum += num
            sum_nums.append(running_sum)
        return sum_nums