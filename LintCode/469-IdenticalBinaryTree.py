"""
Check if two binary trees are identical. Identical means the two binary trees have the same structure and
every identical position has the same value.

Example
    1             1
   / \           / \
  2   2   and   2   2
 /             /
4             4
are identical.

    1             1
   / \           / \
  2   3   and   2   3
 /               \
4                 4
are not identical.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """

    def isIdentical(self, a, b):
        if (not a) ^ (not b):  # 使用not将列表类型转化成bool类型
            return False
        if not a:
            return True
        if a.val == b.val:
            if self.isIdentical(a.left, b.left):
                return self.isIdentical(a.right, b.right)
            else:
                return False
        else:
            return False
