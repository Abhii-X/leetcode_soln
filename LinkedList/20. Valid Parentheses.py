'''
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false'''

#Link:https://leetcode.com/problems/valid-parentheses/description/

#Code:

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s:
            if i =='(' or i == '{' or i =='[':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                x=stack.pop()
                if x!=d[i]:
                    return False
        if len(stack)==0:
            return True
        return False
