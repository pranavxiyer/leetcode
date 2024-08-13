# 3070. Count Submatrices with Top-Left Element and Sum Less Than k
# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
# difficulty: medium

class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        prefix_matrix = [[0 for i in range(cols)] for j in range(rows)]
        
        for r in range(rows):
            prefix_sum = 0
            for c in range(cols):
                prefix_sum += grid[r][c]
                if r == 0:
                    above = 0
                else:
                    above = prefix_matrix[r - 1][c]
                prefix_matrix[r][c] = prefix_sum + above
        
        nums = 0
        for row in prefix_matrix:
            for val in row:
                if val <= k:
                    nums += 1
        return nums