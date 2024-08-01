# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description
# difficulty: easy

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)

        postfix = [0 for i in range(len(nums))]
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            total += nums[i]
            postfix[i] = total

        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        return -1