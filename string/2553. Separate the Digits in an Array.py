'''

Example 1:

Input: nums = [13,25,83,77]
Output: [1,3,2,5,8,3,7,7]
Explanation: 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.'''

#Code:

class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        a=[]
        for i in nums:
            j=0
            while j<len(str(i)):
                a.append(int(str(i)[j]))
                j+=1
            
        return a
