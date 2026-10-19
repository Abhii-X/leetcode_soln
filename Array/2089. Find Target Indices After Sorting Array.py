'''

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.'''

Link:https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=daily-question&envId=2026-10-19

#Code:

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        a=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                a.append(i)
        return a
