# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        first = head
        second = head
        second_pre = None

        i = 0
        while first.next and i < n - 1:
            first = first.next
            i += 1

        if i < n - 1:
            return head

        while first.next:
            second_pre = second
            first = first.next
            second = second.next

        if second_pre is None:
            head = head.next
            del second
        else:
            second_pre.next = second.next
            del second

        return head





        