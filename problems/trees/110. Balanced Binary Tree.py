# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/
# difficulty: easy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node):
            if node is None:
                return [0, True]

            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)

            balanced = left_subtree[1] and right_subtree[1] and abs(left_subtree[0] - right_subtree[0]) <= 1
            return [1 + max(left_subtree[0], right_subtree[0]), balanced]

        return dfs(root)[1]