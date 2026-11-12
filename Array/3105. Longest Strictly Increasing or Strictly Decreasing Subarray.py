'''
Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.'''


Link:https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2026-11-12

#Code:

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        a,b,c=1,1,1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                a+=1
                b=1
            elif nums[i]<nums[i-1]:
                b+=1
                a=1
            else:
                a=1
                b=1
            c=max(c,a,b)
        return c
