# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # convert first list to int
        l_r = self.reverse(l1)
        num1 = self.convertToInt(l_r)

        # convert second list to int
        l_r = self.reverse(l2)
        num2 = self.convertToInt(l_r)

        # sum l1 and l2
        result = num1 + num2 

        # convert sum to lisit
        return self.convertToList(result)

    def convertToInt(self, l: Optional[ListNode]):
        result = l.val
        while (l.next):
            l = l.next
            result = l.val + (result*10)
 
        return result

    def reverse(self, l: Optional[ListNode]):
         # init current, previous, next
        current = l
        previous = next = None

        while (current):
            # store the next node
            next = current.next

            # reverse current node
            current.next = previous
            previous = current
            current = next

        return previous

    def convertToList(self, num):
        final = curr = ListNode(num%10)
        num = num//10
        while num:
            val = num%10
            curr.next = ListNode(val)
            curr = curr.next
            num = num//10

        return final
