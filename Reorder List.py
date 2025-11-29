# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # 1. Find the middle (slow will point to middle)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse the second half
        reversedHead = self.reverse(slow.next)
        slow.next = None   # split the list
        
        # 3. Merge both halves
        first, second = head, reversedHead
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2

    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        