'''
Example:

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]'''


Link:https://leetcode.com/problems/add-two-numbers-ii/description/

#Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        a=""
        temp1=l1
        while temp1:
            a+=str(temp1.val)
            temp1=temp1.next
        b=""
        temp2=l2
        while temp2:
            b+=str(temp2.val)
            temp2=temp2.next
        c=str(int(a)+int(b))
        head=None
        tail=None
        for i in range(len(c)):
            new_Node=ListNode(int(c[i]))
            if head is None:
                head=new_Node
                tail=new_Node
            else:
                tail.next=new_Node
                tail=tail.next
        return head
