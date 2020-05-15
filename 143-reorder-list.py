"""
Given 1->2->3->4, reorder it to 1->4->2->3.

1->2->3->4
1->4->2->3

1->2->3->4
1->2 and 4->3
1->4->2->3

- Find the middle
- Reverse the ll from the middle to end
- Merge first half and reversed second half
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        # Find the middle
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # Reverse slow:
        prev = None
        curr = slow
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # Merge two lists:
        l1 = head
        l2 = prev
        
        while l2.next:
            tmp = l1.next
            l1.next = l2
            l1 = tmp
            
            tmp = l2.next
            l2.next = l1
            l2 = tmp
            
            