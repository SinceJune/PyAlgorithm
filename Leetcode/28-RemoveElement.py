'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''


class Solution(object):
    '''1. 不要在迭代过程中删除元素,会造成index定位错误'''

    '''2. 在函数内部修改外部变量用自加无效,会看成修改局部变量'''

    def removeElement(self, nums, val):
        total = 0
        for num in nums:
            if num == val:
                total = total + 1
        while (total > 0):
            nums.remove(val)
            total = total - 1
        return len(nums)
