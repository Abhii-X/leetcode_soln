'''
Example:
Input: nums = [1,2,3]

Output: true

Explanation:

The middle element of nums is 2, which appears exactly once.

Thus, the answer is true.'''
#Link:https://leetcode.com/problems/unique-middle-element/description/
#Code:
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        a=nums[len(nums)//2]
        if nums.count(a)!=1:
            return False
        else:
            return True
