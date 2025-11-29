#Time C : O(m+n)
#Space C : O(m)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        currA, currB= headA, headB
        lenA, lenB = 0, 0
        while currA:
            currA=currA.next
            lenA+=1
        while currB:
            currB = currB.next
            lenB+=1
        
        while lenA > lenB:
            currA=currA.next
            lenA-=1
        while lenB > lenA:
            currB = currB.next
            lenB -= 1
        while currA != currB:
            currA = currA.next
            currB = currB.next
        return currA

