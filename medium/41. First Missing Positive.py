'''

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.'''

Link:https://leetcode.com/problems/first-missing-positive/description/

#Code:

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        a=[]
        for i in nums:
            if i<=0:
                continue
            else:
                a.append(i)
        b=sorted(list(set(a)))
        print(b)
        m=len(b)+1
        for i in range(len(b)):
            if b[i]!=i+1:
                m=i+1
                break
        return m
