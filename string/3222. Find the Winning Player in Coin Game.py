'''
Example 1:
Input: x = 2, y = 7
Output: "Alice"

Explanation:
The game ends in a single turn:
Alice picks 1 coin with a value of 75 and 4 coins with a value of 10.


Example 2:
Input: x = 4, y = 11
Output: "Bob"

Explanation:
The game ends in 2 turns:
Alice picks 1 coin with a value of 75 and 4 coins with a value of 10.
Bob picks 1 coin with a value of 75 and 4 coins with a value of 10.'''

#Link:https://leetcode.com/problems/find-the-winning-player-in-coin-game/description/

#Code:

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        m=min(x,y//4)
        if m%2==1:
            return "Alice"
        else:
            return "Bob"
