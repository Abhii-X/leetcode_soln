'''

Example :
Input: nums = [1,2,3]
Output: [1,2,3,3,2,1]'''

Link:https://leetcode.com/problems/concatenate-array-with-reverse/description/

#Code:

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        a=nums[::-1]
        return nums+a
