'''
Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".'''
#Link:https://leetcode.com/problems/backspace-string-compare/description/
#Code:
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1=[]
        l2=[]
        for i in s:
            if i=="#":
                if not l1:
                    continue
                else:
                    l1.pop()
            else:
                l1.append(i)
        for i in t:
            if i =="#":
                if not l2:
                    continue
                else:
                    l2.pop()
            else:
                l2.append(i)
        return l1==l2
