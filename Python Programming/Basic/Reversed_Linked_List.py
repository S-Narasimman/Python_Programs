# Problem: Reversed Linked List
# Author: Trl Rizu
# Solution from: Neetcode
# Adapted from: https://leetcode.com/problems/reverse-linked-list/description/

# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example: 
# Input: head = [0,1,2,3]

# Output: [3,2,1,0]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Recursion solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty, return None
        if not head:
            return None

        # Start by assuming the new head is the current node
        newHead = head

        # If there is a next node, recurse until reaching the tail
        if head.next:
            # Recursively reverse the sublist starting from head.next
            newHead = self.reverseList(head.next)

            # After recursion, head.next points to the last node of the reversed sublist
            # So redirect its next pointer back to the current node
            head.next.next = head

        # Break the old link to avoid cycles
        head.next = None

        # Return the new head of the reversed list
        return newHead


#Iteration Solution

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev