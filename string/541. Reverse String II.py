'''

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:

Input: s = "abcd", k = 2
Output: "bacd"'''

#Link:https://leetcode.com/problems/reverse-string-ii/description/

#Code:

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
