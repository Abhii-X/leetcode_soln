'''
Example:
Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.'''
#Link:https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/
#Code:
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        a=[]
        b=0
        for i in nums:
            if i%2==0 and i%3==0:
                a.append(i)
        c=len(a)
        for i in a:
            b+=i
        if c==0:
            return 0
        return b//c
