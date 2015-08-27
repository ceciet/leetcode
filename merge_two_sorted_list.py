# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        result_head = ListNode(0)
        flag = result_head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            flag.next = node
            flag = flag.next

        if l1 is not None:
            flag.next = l1
        if l2 is not None:
            flag.next = l2
        return result_head.next

if __name__  == "__main__":
    s = Solution()
    l1 = ListNode(2)
    l2 = ListNode(1)
    print s.mergeTwoLists(l1, l2)