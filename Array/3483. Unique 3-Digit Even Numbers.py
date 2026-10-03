'''
Example 1:

Input: digits = [1,2,3,4]
Output: 12
Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 
214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is 
only 1 copy of the digit 2.

Example 2:

Input: digits = [0,2,2]
Output: 2
Explanation: The only 3-digit even numbers that can be formed are 202 and 220. 
Note that the digit 2 can be used twice because it appears twice in the array.'''

Link:https://leetcode.com/problems/unique-3-digit-even-numbers/description/

#Code:

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count=0
        l=[]
        for i in permutations(digits,3):
            k=int("".join(map(str,i)))
            if k>99 and k%2==0 and k not  in l:
                l.append(k)
                count+=1
        return count
