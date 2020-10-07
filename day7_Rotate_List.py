# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        
        n = 0
        node = head
        while node:
            n+=1 
            if node.next == None:
                tail = node 
            node = node.next 
            
        k = k%n 
        if k == 0:
            return head 
        
        tail.next = head 
        
        node = head 
        for i in range(n-k-1):
            node = node.next  
        newHead = node.next 
        node.next = None 
        
        return newHead
        
        
