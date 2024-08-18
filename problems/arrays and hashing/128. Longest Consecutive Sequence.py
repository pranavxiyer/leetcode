# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/
# difficulty: medium

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_map = {}
        for num in nums:
            num_map[num] = True
        
        max_seq = 0
        for num in num_map:
            if num - 1 not in num_map:
                seq = 1
                while num + seq in num_map:
                    seq += 1
                max_seq = max(max_seq, seq)
        
        return max_seq