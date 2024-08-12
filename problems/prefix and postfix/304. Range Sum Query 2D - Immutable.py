# 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
# difficulty: medium

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        query_matrix = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
        self.query_matrix = query_matrix
        
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.query_matrix[r][c + 1]
                self.query_matrix[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r1 = row1 + 1
        c1 = col1 + 1
        r2 = row2 + 1
        c2 = col2 + 1
        whole = self.query_matrix[r2][c2]
        above = self.query_matrix[r1 - 1][c2]
        left = self.query_matrix[r2][c1 - 1]
        overlap = self.query_matrix[r1 - 1][c1 - 1]
        return whole - above - left + overlap