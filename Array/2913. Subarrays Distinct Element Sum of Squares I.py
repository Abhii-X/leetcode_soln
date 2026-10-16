'''

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12
+ 22 + 22 + 22 = 15.

Example 2:

Input: nums = [1,1]
Output: 3
Explanation: Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.'''

Link:https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/

#Code:

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        a=[]
        s=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                #a.append(nums[i:j+1])
                x=len(set(nums[i:j+1]))
                s+=x**2
        '''print(a)
        s=0
        for i in range(len(a)):
            x=len(set(a[i]))
            s+=x**2
        print(s)'''
        return s
