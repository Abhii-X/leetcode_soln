'''

Example 1:

Input: n = 12

Output: true

Explanation:

Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
Bob cannot remove 9 stones, so Alice wins.
Example 2:

Input: n = 1

Output: false'''

class Solution:
    def canAliceWin(self, n: int) -> bool:
        def win(n,a,x):
            if a>n:
                return x==0
            x=abs(x-1)
            return win(n-a,a-1,x)
        return win(n,10,1)
