# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/
# difficulty: easy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diameter = [0]

        def dfs(node):
            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            diameter[0] = max(diameter[0], left_height + right_height)
            return 1 + max(left_height, right_height)

        tree_height = dfs(root)
        return diameter[0]