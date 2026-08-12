'''
Example 1:
Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6.
6 is not in the array, therefore 6 is the smallest 
missing integer greater than or equal to the sum of the longest sequential prefix.'''
#Link:https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/?envType=daily-question&envId=2026-08-11
#coe:
class Solution:
    def missingInteger(self, a: list[int]) -> int:
        b=a[0]
        for i in range(1, len(a)):
            if a[i]==a[i-1]+1:
                b+=a[i]
            else:
                break
        while b in a:
            b+=1
        return b
