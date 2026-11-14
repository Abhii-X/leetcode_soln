'''

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]'''

Link:https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

#Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        a = []
        curr = head
        while curr is not None:
            a.append(curr.val)
            curr = curr.next
        print(a)
        f={}
        for i in a:
            f[i] = f.get(i, 0) + 1
        print(f)
        b = []
        for i, j in f.items():
            if j == 1:
                b.append(i)
            else:
                continue
        print(b)
        root = None
        tail = None
        for i in range(len(b)):
            new_Node = ListNode(b[i])
            if root is None:
                root = new_Node
                tail = new_Node
            else:
                tail.next = new_Node
                tail = tail.next
        return root
