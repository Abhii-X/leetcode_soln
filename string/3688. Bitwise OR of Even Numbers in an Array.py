'''

Example 1:

Input: nums = [1,2,3,4,5,6]
Output: 6
Explanation:
The even numbers are 2, 4, and 6. Their bitwise OR equals 6.

Example 2:
Input: nums = [7,9,11]
Output: 0
Explanation:
There are no even numbers, so the result is 0.'''

Link:https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/description/

#Code:

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if i%2==0:
                c=c|i
        return c
