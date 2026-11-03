'''
Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
Example 2:

Input: nums = [1,1,1]
Output: 0'''

Link:https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/

#Code:


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        a=min(nums)
        s=0
        for i in range(len(nums)):
            s+=(nums[i]-a)
        return s
