'''
Example 1:

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.'''

Link:https://leetcode.com/problems/arranging-coins/description/

#Code:

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return 1
        c=0
        a=n
        for i in range(n):
            if a<i+1:
                return c
            else:
                a-=(i+1)
                c+=1
