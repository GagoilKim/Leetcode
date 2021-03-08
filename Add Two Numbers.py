# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = l1
        num1 = []
        while tmp.next != None:
            num1.insert(0, str(tmp.val))
            tmp = tmp.next
        num1.insert(0, str(tmp.val))
        num1 = ''.join(num1)
        
        tmp = l2
        num2 = []
        while tmp.next != None:
            num2.insert(0, str(tmp.val))
            tmp = tmp.next
        num2.insert(0, str(tmp.val))
        num2 = ''.join(num2)
        total = (int(num1) + int(num2))
        result = [int(x) for x in str(total)]
        print(result)
        
        tmp = None
        for i in range(len(result)):
            now = ListNode(result[i], None)
            if tmp != None:
                now.next = tmp
                tmp = now
            else:
                tmp = now
        return (tmp)