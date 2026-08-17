'''Example:
Input: s = "1112"

Output: "1112"

Explanation:

The string already represents the largest possible even number, so no deletions are needed.'''
#Link:https://leetcode.com/problems/largest-even-number/description/
#Code:
class Solution:
    def largestEven(self, a: str) -> str:
        b = len(a) - 1
        while b >= 0:
            if int(a[b]) % 2 == 0:
                return a[:b + 1]
            b -= 1
        return ""
