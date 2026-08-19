'''
Example:
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.'''
#Link:https://leetcode.com/problems/baseball-game/description/
#Code:
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        b=0
        for i in range(len(operations)):
            if operations[i] not in 'CD+':
                a.append(int(operations[i]))
            elif operations[i]=='C':
                a.pop()
            elif operations[i]=='D':
                a.append(2*a[-1])
            elif operations[i]=='+':
                a.append(a[-1]+a[-2])
        for i in a:
            b+=int(i)
        return b
