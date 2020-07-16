# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# We can use a stack that stores nodes in monotone decreasing order of value. When we see a node_j with a larger value, every node_i in the stack has next_larger(node_i) = node_j.

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result = []
        stack = []
        
        idx = -1
        
        while head:
            idx += 1
            result.append(0)
            while stack and stack[-1][1] < head.val:
                i, val = stack.pop()
                result[i] = head.val
            stack.append((idx, head.val))
            head = head.next
            
        return result
        