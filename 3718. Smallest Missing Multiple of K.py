'''Example:Example 1:

Input: nums = [8,2,3,4,6], k = 2

Output: 10

Explanation:

The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from nums is 10'''

#Link:https://leetcode.com/problems/smallest-missing-multiple-of-k/description/
#Code:
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        c=k
        for i in range(1,len(nums)+2):
            if i*c not in nums:
                return i*c
