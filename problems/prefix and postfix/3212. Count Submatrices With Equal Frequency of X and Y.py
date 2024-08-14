# 3212. Count Submatrices With Equal Frequency of X and Y
# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description/
# difficulty: medium

class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        prefix_matrix = [['' for i in range(cols)] for j in range(rows)]

        for r in range(rows):
            prefix_x = 0
            prefix_y = 0
            for c in range(cols):
                if r == 0:
                    above_x = 0
                    above_y = 0
                else:
                    above_x = prefix_matrix[r - 1][c][0]
                    above_y = prefix_matrix[r - 1][c][1]
                if grid[r][c] == "X":
                    prefix_x += 1
                elif grid[r][c] == "Y":
                    prefix_y += 1
                prefix_matrix[r][c] = (prefix_x + above_x, prefix_y + above_y)

        nums = 0
        for row in prefix_matrix:
            for tuple in row:
                if tuple[0] > 0 and tuple[0] == tuple[1]:
                    nums += 1
        return nums