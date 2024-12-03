# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.getDepth(root) >= 0

    def getDepth(self, root):
        if root:
            l_depth = self.getDepth(root.left)
            r_depth = self.getDepth(root.right)
            if abs(l_depth - r_depth) > 1 or l_depth < 0 or  r_depth < 0:
                return -1
            else:
                return 1 + max(l_depth, r_depth)
        else:
            return 0