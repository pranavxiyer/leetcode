# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/
# difficulty: easy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        left_child = root.left
        right_child = root.right
        root.left = right_child
        root.right = left_child
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root