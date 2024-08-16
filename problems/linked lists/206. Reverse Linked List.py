# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/
# difficulty: easy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head != None:
            temp = head.next
            head.next = prev

            prev = head
            head = temp
        return prev

        # without directly using head
        # curr = head
        # prev = None
        # while curr != None:
        #     temp = curr.next
        #     curr.next = prev

        #     prev = curr
        #     curr = temp
        # return prev