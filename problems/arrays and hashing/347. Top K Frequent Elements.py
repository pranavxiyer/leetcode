# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/
# difficulty: medium

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_map = {}

        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1
        
        freq_list = []
        for i in range(k):
            top_freq_num = max(num_map, key = lambda x: num_map[x])
            freq_list.append(top_freq_num)
            num_map[top_freq_num] = -1
        return freq_list

        # solution 2, without using max func
        # freq_list = []
        # cur_max = [-1, -1]
        # for i in range(k):
        #     for num in num_map:
        #         num_frequency = num_map[num]
        #         if num_frequency >= cur_max[1] and num not in freq_list:
        #             cur_max = [num, num_frequency]
        #     freq_list.append(cur_max[0])
        #     cur_max = [-1, -1]

        # return freq_list