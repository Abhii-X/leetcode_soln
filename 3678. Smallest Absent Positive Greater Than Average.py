'''
Return the smallest absent positive integer in nums such that it is strictly greater than the average of all elements in nums.

The average of an array is defined as the sum of all its elements divided by the number of elements.
 

Example 1:

Input: nums = [3,5]

Output: 6

Explanation:

The average of nums is (3 + 5) / 2 = 8 / 2 = 4.
The smallest absent positive integer greater than 4 is 6.
Example 2:

Input: nums = [-1,1,2]

Output: 3

Explanation:

​​​​​​​The average of nums is (-1 + 1 + 2) / 3 = 2 / 3 = 0.667.
The smallest absent positive integer greater than 0.667 is 3.
Example 3:

Input: nums = [4,-1]

Output: 2

Explanation:

The average of nums is (4 + (-1)) / 2 = 3 / 2 = 1.50.
The smallest absent positive integer greater than 1.50 is 2.'''


Link:https://leetcode.com/problems/smallest-absent-positive-greater-than-average/description/
#Code:

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        a=sum(nums)
        b=a//len(nums)
        x=1
        c=max(nums)+len(nums)+2
        for i in range(max(1,b+1),10000):
            if i not in nums:
                x=i
                break
        return x
