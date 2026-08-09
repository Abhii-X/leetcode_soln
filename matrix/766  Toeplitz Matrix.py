'''Example:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.'''
link:https://leetcode.com/problems/toeplitz-matrix/description/
code:
class Solution:
    def isToeplitzMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True
