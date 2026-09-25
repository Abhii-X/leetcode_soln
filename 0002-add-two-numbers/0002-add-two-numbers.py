# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        a=""
        temp=l1
        while temp is not None:
            a+=str(temp.val)
            temp=temp.next
        print(a)
        b=""
        root=l2
        while root is not None:
            b+=str(root.val)
            root=root.next
        print(b)
        c=str(int(a[::-1])+int(b[::-1]))
        print(c)
        d=c[::-1]
        print(list(d))
        head=None
        tail=None
        for i in range(len(d)):
            new_node=ListNode(int(d[i]))
            if head is None:
                head=new_node
                tail=new_node
            else:
                tail.next=new_node
                tail=tail.next
        return head