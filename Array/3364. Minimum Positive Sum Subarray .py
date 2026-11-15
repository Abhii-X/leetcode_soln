'''

Example 1:

Input: nums = [3, -2, 1, 4], l = 2, r = 3

Output: 1

Explanation:

The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:

[3, -2] with a sum of 1
[1, 4] with a sum of 5
[3, -2, 1] with a sum of 2
[-2, 1, 4] with a sum of 3
Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

Example 2:

Input: nums = [-2, 2, -3, 1], l = 2, r = 3

Output: -1

Explanation:

There is no subarray of length between l and r that has a sum greater than 0. So, the answer is -1.

Example 3:

Input: nums = [1, 2, 3, 4], l = 2, r = 4

Output: 3

Explanation:

The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3.'''

Link:https://leetcode.com/problems/minimum-positive-sum-subarray/description/

#Code:


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        a = []
        def s(nums, l, r):
            if l > r:
                return
            i = 0
            while i + l <= len(nums):
                total = 0
                for j in range(i, i + l):
                    total += nums[j]
                if total > 0:
                    a.append(total)
                i += 1
            s(nums, l + 1, r)
        s(nums, l, r)
        if len(a) == 0:
            return -1
        return min(a)
