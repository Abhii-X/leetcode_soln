'''
Example:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]'''

Link:https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

#Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr=head
        a=[]
        while curr is not None:
            a.append(curr.val)
            curr=curr.next
        b=len(a)-n
        print(a[b])
        c=[]
        for i in range(len(a)):
            if i==b:
                continue
            else:
                c.append(a[i])
        print(c)
        root=None
        tail=None
        for i in range(len(c)):
            new_node=ListNode(c[i])
            if root is None:
                root=new_node
                tail=new_node
            else:
                tail.next=new_node
                tail=tail.next
        return root
