# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        p = head
        q = head.next

        while q is not None:
            while q is not None and q.val == p.val:
                q = q.next
            if q is None:
                p.next = q
                continue
            p.next = q
            p = p.next
            q = p.next
        return head