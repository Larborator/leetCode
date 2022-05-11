"""
https://leetcode.cn/problems/count-nodes-equal-to-average-of-subtree/

author: labuladuo
date: 2022/5/10
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    __ans = 0

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.deep(root)
        return self.__ans

    def deep(self, root: Optional[TreeNode]) -> tuple:
        if root is None:
            return 0, 0
        left = self.deep(root.left)
        right = self.deep(root.right)
        sum = left[0] + right[0] + root.val
        cnt = left[1] + right[1] + 1
        if root.val == sum // cnt:
            self.__ans += 1
        return sum, cnt


if __name__ == '__main__':
    t = TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))
    s = Solution()
    res = s.averageOfSubtree(t)
    print(res)
