'''
"Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0),
you will get the maximum value,
that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.'''
link is:https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
code:class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=float('-inf')
        c=1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                c=(nums[i]-1)*(nums[j]-1)
                maxi=max(maxi,c)
        return maxi
