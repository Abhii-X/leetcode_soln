'''
Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13


Example 2:
Input: matrix = [[-5]], k = 1
Output: -5'''

#Link:https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#Code:
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l=[]
        for i in matrix:
            for j in i:
                l.append(j)
        l.sort()
        return l[k-1]
