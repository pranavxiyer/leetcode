# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/description/
# difficulty: hard

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_map = {}
        for char in t:
            t_map[char] = 1 + t_map.get(char, 0)
        
        s_map = {}
        have, need = 0, len(t_map)
        l = 0
        r = 0
        min_window = float("inf")
        min_string = ""
        while r < len(s):
            char = s[r]
            s_map[char] = 1 + s_map.get(char, 0)
            if char in t_map and s_map[char] == t_map[char]:
                have += 1
            
            while have == need:
                min_window = min(min_window, r - l + 1)
                if min_window == r - l + 1:
                    min_string = s[l:r+1]
                
                left_char = s[l]
                if left_char in t_map and s_map[left_char] - 1 < t_map[left_char]:
                    have -= 1
                s_map[left_char] -= 1
                l += 1

            r += 1
        
        return min_string