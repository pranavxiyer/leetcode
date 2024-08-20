# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/
# difficulty: hard

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max_heights = [0 for i in range(len(height))]
        left_max = 0
        for l in range(1, len(height)):
            left_max = max(left_max, height[l-1])
            left_max_heights[l] = left_max

        right_max_heights = [0 for i in range(len(height))]
        right_max = 0
        for r in range(len(height) - 2, -1, -1):
            right_max = max(right_max, height[r+1])
            right_max_heights[r] = right_max
        
        total_rain = 0
        for i in range(len(height)):
            total_rain += max(0, min(left_max_heights[i], right_max_heights[i]) - height[i])
        return total_rain