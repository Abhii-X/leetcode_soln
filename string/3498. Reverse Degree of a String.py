'''Example 1:

Input: s = "abc"

Output: 148

Explanation:

Letter	Index in Reversed Alphabet	Index in String	Product
'a'	26	1	26
'b'	25	2	50
'c'	24	3	72
The reversed degree is 26 + 50 + 72 = 148.

Example 2:

Input: s = "zaza"

Output: 160

Explanation:

Letter	Index in Reversed Alphabet	Index in String	Product
'z'	1	1	1
'a'	26	2	52
'z'	1	3	3
'a'	26	4	104
The reverse degree is 1 + 52 + 3 + 104 = 160.'''


#Link:https://leetcode.com/problems/reverse-degree-of-a-string/description/

#Code:

class Solution:
    def reverseDegree(self, s: str) -> int:
        b=0
        i=0
        while i<len(s):
            b+=(123-ord(s[i]))*(i+1)
            i+=1
        return b
