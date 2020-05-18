# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
First take: 
    - Time complexity: O(n) - 2 passes
    - Space complexity: O(2n) -> O(n)
Seperate the ll into 2 lls 
Merge 2 lls together into one
"""
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        curr = head
        
        odd = ListNode(0)
        currOdd = odd
        
        even = ListNode(0)
        currEven = even
        
        isOdd = True
        
        # Form 2 lls, odd and even
        while curr:
            node = ListNode(curr.val)
            if isOdd:
                currOdd.next = node
                currOdd = currOdd.next
                isOdd = False
            else:
                currEven.next = node
                currEven = currEven.next
                isOdd = True
            curr = curr.next
            
        odd = odd.next
        even = even.next
            
        # Merge 2 lls
        
        # Find tail of odd
        tail = odd
        while tail and tail.next:
            tail = tail.next
            
        # Merge even into tail of odd
        tail.next = even
        
        return odd
        
