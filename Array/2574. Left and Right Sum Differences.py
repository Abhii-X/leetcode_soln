'''

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].'''

#Link:https://leetcode.com/problems/left-and-right-sum-differences/description/

#Code:

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=0
        a=[]
        for i in range(len(nums)):
            if i==0:
                a.append(0)
            else:
                l+=nums[i-1]
                a.append(l)
        b=[]
        r=sum(nums)
        for i in range(len(nums)):
            if i==len(nums)-1:
                b.append(0)
            else:
                r-=nums[i]
                b.append(r)
        c=[]
        for i in range(len(nums)):
            c.append(abs(a[i]-b[i]))
        return c
