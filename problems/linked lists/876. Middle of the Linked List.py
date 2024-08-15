# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/
# difficulty: easy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast_ptr = head
        slow_ptr = head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        
        return slow_ptr