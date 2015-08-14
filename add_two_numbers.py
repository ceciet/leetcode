# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        root = ListNode((l1.val+l2.val)%10)
        result = root
        flag = (l1.val+l2.val)/10
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            val = (l1.val + l2.val + flag)%10
            flag = (l1.val + l2.val + flag)/10
            node = ListNode(val)
            root.next = node
            root = root.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = (l1.val + flag)%10
            flag = (l1.val + flag)/10
            node = ListNode(val)
            root.next = node
            root = root.next
            l1 = l1.next
        while l2 :
            val = (l2.val + flag)%10
            flag = (l2.val + flag)/10
            node = ListNode(val)
            root.next = node
            root = root.next
            l2 = l2.next
        if flag!=0:
            node = ListNode(flag)
            root.next= node
        return result