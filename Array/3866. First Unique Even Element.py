'''Example:
Input: nums = [3,4,2,5,4,6]

Output: 2

Explanation:

Both 2 and 6 are even and they appear exactly once. Since 2 occurs first in the array, the answer is 2.'''
#Link:https://leetcode.com/problems/first-unique-even-element/description/
#Code:
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for i in nums:
            if i%2==0 and nums.count(i)==1:
                return i
        return -1
