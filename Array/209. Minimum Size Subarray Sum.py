'''Example:
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1'''
#link:https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=array
#code:
class Solution:
    def minSubArrayLen(self, target, nums):
        l=0
        count=0
        a=float('inf')
        for i in range(len(nums)):
            count+=nums[i]
            while count>=target:
                a=min(a,i-l+1)
                count-=nums[l]
                l+=1
        if a==float('inf'):
            return 0
        return a
