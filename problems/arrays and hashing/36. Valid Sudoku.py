# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/
# difficulty: medium

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {} # maps row index -> list of numbers in that row
        cols = {} # maps col index -> list of numbers in that col
        subsquares = {} # maps tuple -> list of numbers in that sub square

        for r in range(9):
            rows[r] = []
            for c in range(9):
                cols[c] = []
                s_r, s_c = r // 3, c // 3
                subsquares[(s_r, s_c)] = []

        for r in range(9):
            for c in range(9):
                s_r, s_c = r // 3, c // 3
                square = board[r][c]
                if square == ".":
                    continue
                if square in rows[r] or square in cols[c] or square in subsquares[(s_r, s_c)]:
                    return False
                rows[r].append(square)
                cols[c].append(square)
                subsquares[(s_r, s_c)].append(square)
        return True
