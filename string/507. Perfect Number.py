'''

Example:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.'''

Link:https://leetcode.com/problems/perfect-number/description/

#Code:

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6,28,496,8128,33550336]
