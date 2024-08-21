# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# difficulty: medium

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_map = {}
        max_len = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in str_map:
                str_map[s[r]] = True
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                l += 1
                r = l
                str_map = {}
        return max_len