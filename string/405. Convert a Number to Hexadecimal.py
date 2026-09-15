'''

Example 1:

Input: num = 26
Output: "1a"

Example 2:

Input: num = -1
Output: "ffffffff"'''

#Link:https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

#Code:

class Solution:
    def toHex(self, num: int) -> str:
        if num<0:
            num=num+(1<<32)
        if num>0:
            he="0123456789abcdef"
            a=''
            while num>0:
                r=num%16
                a=he[r]+a
                num=num//16
            return a
        if num==0:
            return "0"
