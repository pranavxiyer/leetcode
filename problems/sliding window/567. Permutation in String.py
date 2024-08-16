# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/
3 # difficulty: medium

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_map = {}
        for char in s1:
            if char in s1_map:
                s1_map[char] += 1
            else:
                s1_map[char] = 1
        
        l = 0
        r = 0
        s2_map = {}

        while r < len(s2):
            char_to_add = s2[r]
            if char_to_add in s2_map:
                s2_map[char_to_add] += 1
            else:
                s2_map[char_to_add] = 1

            if r - l != len(s1) - 1:
                r += 1
            else:
                match = True
                for char in s1_map:
                    if char not in s2_map or s2_map[char] != s1_map[char]:
                        match = False
                        break
                if match:
                    return True
                else:
                    s2_map[s2[l]] -= 1
                    r += 1
                    l += 1
        return False
    
        # solution that was too slow
        # s1_perm = ''.join(sorted(s1))
        # l = 0
        # r = len(s1_perm) - 1
        # while l + r < len(s2):
        #     s2_substr = s2[l:l+r+1]
        #     sorted_s2 = ''.join(sorted(s2_substr))
        #     if s1_perm == sorted_s2:
        #         return True
        #     l += 1
        # return False