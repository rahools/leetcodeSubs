#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initialize the return var
        strt = None
        if l1 != None and l2 != None:
            if l1.val > l2.val:
                strt = ListNode(l2.val)
                l2 = l2.next
            else:
                strt = ListNode(l1.val)
                l1 = l1.next
        else:
            if l1 != None:
                strt = ListNode(l1.val)
                l1 = l1.next
            elif l2 != None:
                strt = ListNode(l2.val)
                l2 = l2.next
            else:
                return strt

            
        temp = strt
        # loop Lists
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            else:
                temp.next = ListNode(l1.val)
                l1 = l1.next

            temp = temp.next

        # add remaining Elements
        while l1 != None:
            temp.next = ListNode(l1.val)
            l1 = l1.next
            temp = temp.next

        while l2 != None:
            temp.next = ListNode(l2.val)
            l2 = l2.next
            temp = temp.next

        return strt

# @lc code=end

