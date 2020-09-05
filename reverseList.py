# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        vals = []
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            while head.next != None:
                v = head.val
                vals.append(v)
                head = head.next
            vals.append(head.val)

            v = vals.reverse()
            result = ListNode(0, None)
            tmp = result
            for i in vals:
                cur = ListNode(i, None)
                tmp.next = cur
                tmp = tmp.next


            return result.next