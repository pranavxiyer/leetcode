# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable
# difficulty: easy

# input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

# output
# [null, 1, -1, -3]
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

        summed = []
        total = 0
        for num in nums:
            total += num
            summed.append(total)

        self.summed = summed

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.summed[right]
        else:
            return self.summed[right] - self.summed[left - 1]