'''

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0'''

Link:https://leetcode.com/problems/add-digits/description/

#Code:

class Solution:
    def addDigits(self, num: int) -> int:
        def digits(num,s):
            if num<10:
                return num
            else:
                while num>0:
                    m=num%10
                    s+=m
                    num//=10
                return digits(s,0)
        if len(str(num))==1:
            return num
        else:
            return digits(num,0)
