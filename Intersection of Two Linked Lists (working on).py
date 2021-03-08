# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tmpA = headA
        tmpB = headB
#       A part
        valueA = [tmpA.val]
        while tmpA.next != None:
            tmpA = tmpA.next
            valueA.append(tmpA.val)
#       B part
        valueB = [tmpB.val]
        while tmpB.next != None:
            tmpB = tmpB.next
            valueB.append(tmpB.val)
        dif = len(valueA) - len(valueB) 
        if dif > 0:
            valueA = valueA[dif:]
        else:
            dif *= -1
            valueB = valueB[dif:]
            print(valueB)
        