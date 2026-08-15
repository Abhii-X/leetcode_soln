'''Example:
Input: bulbs = [10,30,20,10]

Output: [20,30]

Explanation:

The bulbs[0] = 10th light bulb is currently off. We switch it on.
The bulbs[1] = 30th light bulb is currently off. We switch it on.
The bulbs[2] = 20th light bulb is currently off. We switch it on.
The bulbs[3] = 10th light bulb is currently on. We switch it off.
In the end, the 20th and the 30th light bulbs are on.'''
#Link:https://leetcode.com/problems/toggle-light-bulbs/description/
#Code:
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        a=[]
        for i in bulbs:
            if bulbs.count(i)%2!=0 and i not in a:
                a.append(i)
        a.sort()
        return a
