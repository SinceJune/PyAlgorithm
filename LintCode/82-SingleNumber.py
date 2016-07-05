"""
Given 2*n + 1 numbers, every numbers occurs twice except one, find it.

Example
Given [1,2,2,1,3,4,3], return 4
"""


class Solution:
    """
    @param A : an integer array
    @return : a integer
    """

    def singleNumber(self, A):
        # 位运算,自身与自身异或为0,与0异或为自身
        temp = 0
        for i in A:
            temp = temp ^ i
        return temp
