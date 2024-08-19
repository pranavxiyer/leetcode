# 15. 3Sum
# https://leetcode.com/problems/3sum/description/
# difficulty: medium

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sum_list = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            first_num = nums[i]
            l = i + 1
            r = len(nums) - 1
            target = 0 - first_num
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    triplet = [nums[i], nums[l], nums[r]]
                    sum_list.append(triplet)
                    while l < r and nums[l] == triplet[1]:
                        l += 1
                    while l < r and nums[r] == triplet[2]:
                        r -= 1
        
        return sum_list

        # sum_list = []

        # for i in range(len(nums)):
        #     first = nums[i]
        #     target = 0 - first
        #     sum_map = {}
        #     two_sum = []
        #     for j in range(i+1, len(nums)):
        #         num = nums[j]
        #         diff = target - num
        #         if diff in sum_map:
        #             two_sum.append([sum_map[diff], j])
        #         sum_map[num] = j

        #     for pair in two_sum:
        #         second = nums[pair[0]]
        #         third = nums[pair[1]]

        #         sums = [first, second, third]
        #         sums.sort()
        #         if sums not in sum_list:
        #             sum_list.append(sums)
        # return sum_list