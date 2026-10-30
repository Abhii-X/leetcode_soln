'''
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 '''
Link:https://leetcode.com/problems/rotate-list/description/?envType=problem-list-v2&envId=linked-list
#Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        a=[]
        root = head
        while root is not None:
            a.append(root.val)
            root=root.next
        if len(a)==0:
            return None
        if k==0:
            return head
        else:
            k=k%len(a)
        r=a[-k:]+a[:-k]
        curr=None
        tail=None
        for i in range(len(r)):
            new_Node=ListNode(r[i])
            if curr is None:
                curr=new_Node
                tail=new_Node 
            else:
                tail.next=new_Node
                tail=tail.next
        return curr
