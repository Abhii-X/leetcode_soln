'''

Example 1:

Input: order = [3,1,2,5,4], friends = [1,3,4]
Output: [3,1,4]
Explanation:
The finishing order is [3, 1, 2, 5, 4]. Therefore, the finishing order of your friends is [3, 1, 4].

Example 2:
Input: order = [1,4,5,3,2], friends = [2,5]
Output: [5,2]
Explanation:
The finishing order is [1, 4, 5, 3, 2]. Therefore, the finishing order of your friends is [5, 2].'''

Link:https://leetcode.com/problems/restore-finishing-order/description/

#Code:

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        a=[]
        for i in order:
            if i in friends:
                a.append(i)
            else:
                continue
        return a
