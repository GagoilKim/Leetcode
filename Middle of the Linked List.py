# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cur = head
        count = 1
        while cur.next != None:
            cur = cur.next
            count += 1
        result = head
        if count % 2 == 0:
            count = int(count / 2)
            for i in range(count):
                result = result.next            
        else:
            count = int(count/2)
            for i in range(count):
                result = result.next
        return result
            