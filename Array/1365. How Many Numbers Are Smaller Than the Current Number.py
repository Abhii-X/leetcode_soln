'''
Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).'''

Link:https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
#Code:
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        i=0
        while i<len(nums):
            c=0
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]>nums[j]:
                        c+=1
            a.append(c)
            i+=1
        return a
