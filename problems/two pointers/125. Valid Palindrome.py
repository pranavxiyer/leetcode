# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/
# difficulty: easy

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        l_s = ""
        r_s = ""

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                l_s += s[l].lower()
                r_s += s[r].lower()
                l += 1
                r -= 1
        return l_s == r_s