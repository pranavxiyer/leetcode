# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description
# difficulty: medium

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        postfix = [1 for i in range(len(nums))]
        answer = []

        prefix_total = 1
        for i in range(len(nums)):
            prefix_total *= nums[i]
            prefix.append(prefix_total)

        postfix_total = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix_total *= nums[i]
            postfix[i] = postfix_total

        for i in range(len(nums)):
            if i == 0:
                left = 1
                right = postfix[i + 1]
            elif i == len(nums) - 1:
                right = 1
                left = prefix[i - 1]
            else:
                left = prefix[i - 1]
                right = postfix[i + 1]
            answer.append(left * right)
        
        return answer