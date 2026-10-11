'''

Example 1:

Input: nums = [1,2,3,4]
Output: 21
Explanation: There are exactly 3 special elements in nums: nums[1] since 1 
divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
Hence, the sum of the squares of all special elements of nums is
nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.  

Example 2:

Input: nums = [2,7,1,19,18,3]
Output: 63
Explanation: There are exactly 4 special elements in nums:
nums[1] since 1 divides 6, nums[2] since 2 divides 6, nums[3] since 3 divides 6, 
and nums[6] since 6 divides 6. 
Hence, the sum of the squares of all special elements of nums is 
nums[1] * nums[1] + nums[2] * nums[2] + nums[3] * nums[3] + nums[6] * nums[6] =
2 * 2 + 7 * 7 + 1 * 1 + 3 * 3 = 63. '''


Link:https://leetcode.com/problems/sum-of-squares-of-special-elements/description/?envType=daily-question&envId=2026-10-11

#Code:

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum=0
        a=[]
        x=len(nums)
        for i in range(1,x+1):
            if x%(i)==0:
                a.append(nums[i-1])
            else:
                continue
        for i in range(len(a)):
            sum+=a[i]*a[i]
        return sum
