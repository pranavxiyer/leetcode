# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/
# difficulty: easy

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_word_map = {}
        for char in s:
            if char in s_word_map:
                s_word_map[char] += 1
            else:
                s_word_map[char] = 1
        
        t_word_map = {}
        for char in t:
            if char in t_word_map:
                t_word_map[char] += 1
            else:
                t_word_map[char] = 1

        return s_word_map == t_word_map