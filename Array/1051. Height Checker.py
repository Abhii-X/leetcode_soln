'''
Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.'''

#Link:https://leetcode.com/problems/height-checker/description/

#Code:

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=[]
        for i in heights:
            l.append(i)
        l.sort()
        count=0
        for i in range(len(l)):
            if heights[i]!=l[i]:
                count+=1
        return count
