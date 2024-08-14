# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/
# difficulty: easy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        merged_start = ListNode()
        merged_ptr = merged_start

        while list1 and list2:
            if list1.val <= list2.val:
                merged_ptr.next = list1
                list1 = list1.next
            else:
                merged_ptr.next = list2
                list2 = list2.next
            merged_ptr = merged_ptr.next
        
        if list1:
            merged_ptr.next = list1
        else:
            merged_ptr.next = list2
            
        return merged_start.next