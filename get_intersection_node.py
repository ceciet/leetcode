# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        len1 = 0
        len2 = 0

        p = headA
        q = headB

        while p is not None:
            p = p.next
            len1 += 1

        while q is not None:
            q = q.next
            len2 += 1

        if len1 > len2:
            p = headA
            q = headB
        else:
            q = headA
            p = headB

        i = 0
        while i < abs(len2 - len1):
            p = p.next
            i += 1

        while p is not None and q is not None:
            if p.val == q.val:
                return p
            p = p.next
            q = q.next

        return None


if __name__ == '__main__':
    s = Solution()

    headA = ListNode(10)
    headA.next = ListNode(20)
    headB = ListNode(10)
    my_answer = s.getIntersectionNode(headA, headB)
    print my_answer.val

