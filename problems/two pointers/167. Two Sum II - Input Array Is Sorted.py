# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# difficulty: medium

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r]  > target:
                r -= 1
            else:
                l += 1
        return [l + 1, r + 1]
        
        # solution 2, little more confusing lowkey
        # while l < r:
        #     if numbers[l] + numbers[r]  > target:
        #         r -= 1
        #     elif numbers[l] + numbers[r]  < target:
        #         l += 1
        #     else:
        #         return [l + 1, r + 1]
