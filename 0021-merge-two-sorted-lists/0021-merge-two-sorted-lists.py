# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        a=[]
        temp=list1
        while temp is not None:
            a.append(temp.val)
            temp=temp.next
        curr=list2
        while curr is not None:
            a.append(curr.val)
            curr=curr.next
        a.sort()
        head=None
        tail=None
        for i in range(len(a)):
            new_Node=ListNode(a[i])
            if head is None:
                head=new_Node
                tail=new_Node
            else:
                tail.next=new_Node
                tail=tail.next
        return head