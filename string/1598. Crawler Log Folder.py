'''
Example:
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.'''
#Link:https://leetcode.com/problems/crawler-log-folder/description/
#Code:
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        a=[]
        for i in range(len(logs)):
            if logs[i] == '../':
                if not a:
                    continue
                else:
                    a.pop()
            elif logs[i]=='./':
                continue
            else:
                a.append(logs[i])
        b=len(a)
        return b
