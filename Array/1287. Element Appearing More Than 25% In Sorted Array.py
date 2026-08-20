'''
Example:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1'''
#Link:https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/
#Code:
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=0
        for i in arr:
            if arr.count(i) > count:
                count=arr.count(i)
                c=i
        return c
