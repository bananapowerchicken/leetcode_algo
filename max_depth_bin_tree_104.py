# https://leetcode.com/problems/maximum-depth-of-binary-tree
# complexity: easy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # should be recursive
    def maxDepth(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        if root:
            left_path_len = self.maxDepth(root.left)
            right_path_len = self.maxDepth(root.right)
        
        print('AAA', left_path_len, right_path_len)
        
        return 1+max(left_path_len, right_path_len)



def test():
    r = TreeNode(1, 2, 2)
    sol = Solution()
    assert sol.maxDepth(r) == 2


if __name__ == '__main__':
    test()