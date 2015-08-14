__author__ = 'baidu'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        l = []
        node = head
        while node != None:
            l.append(node.val)
            node = node.next
        return l == l[::-1]