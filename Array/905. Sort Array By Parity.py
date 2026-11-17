'''

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 '''

Link:https://leetcode.com/problems/sort-array-by-parity/description/

#Code:

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i,j=0,len(nums)-1
        while i<j:
            if nums[i]%2==0 and nums[j]%2!=0:
                j-=1
                i+=1
            elif nums[i]%2!=0 and nums[j]%2==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            elif nums[i]%2!=0 and nums[j]%2!=0:
                j-=1
            else:
                i+=1
        return nums
