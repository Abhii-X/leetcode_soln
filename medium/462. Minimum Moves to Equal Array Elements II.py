'''
Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16'''

Link:https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/

#Code:

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        a=sorted(nums)
        b=len(a)//2
        s=0
        for i in range(len(a)):
            s=s+abs((a[b]-a[i]))
        return s
