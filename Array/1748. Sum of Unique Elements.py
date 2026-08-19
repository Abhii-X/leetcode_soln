'''
Example:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.'''
Link:https://leetcode.com/problems/sum-of-unique-elements/description/
#Code:
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if nums.count(i)==1:
                a.append(i)
        print(a)
        s=0
        for i in a:
            s+=i
        return s
