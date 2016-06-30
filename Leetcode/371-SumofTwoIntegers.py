"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        c = a ^ b;
        d = (a & b) << 1
        return self.getSum(c, d)


s = Solution()
print(s.getSum(-1, 2))
