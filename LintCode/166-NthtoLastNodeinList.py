"""
Find the nth to last element of a singly linked list.

The minimum number of nodes in list is n.

Example
Given a List  3->2->1->5->null and n = 2, return node  whose value is 1.
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list.
    """

    def nthToLast(self, head, n):
        tail = head
        while n > 0:
            head = head.next
            n -= 1;
        while head:
            head = head.next
            tail = tail.next
        return tail.val
