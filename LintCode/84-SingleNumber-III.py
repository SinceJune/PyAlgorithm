"""
Given 2*n + 2 numbers, every numbers occurs twice except two, find them.

Example
Given [1,2,2,3,4,4,5,3] return 1 and 5

Challenge
O(n) time, O(1) extra space.
"""


class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """

    def singleNumberIII(self, A):
        num = 0
        for i in A:
            num = num ^ i
        circle = 0
        tmp = num
        num1 = num
        num2 = num
        while tmp % 2 == 0:
            tmp = tmp >> 1
            circle = circle + 1
        for i in A:
            tmp = i >> circle
            if tmp % 2:
                num1 = num1 ^ i
            else:
                num2 = num2 ^ i
        return num1, num2
