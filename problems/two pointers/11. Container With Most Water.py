# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# difficulty: medium

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_amt = 0
        l = 0
        r = len(height) - 1

        while l < r:
            cont_width = r - l
            cont_height = min(height[l], height[r])
            amt = cont_width * cont_height
            max_amt = max(max_amt, amt)
            if cont_height == height[l]:
                l += 1
            else:
                r -= 1
        return max_amt