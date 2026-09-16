'''

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]'''

#Link:https://leetcode.com/problems/repeated-dna-sequences/description/

#Code

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        a=[]
        d=set()
        c=set()
        for i in range(len(s)-9):
            b=s[i:i+10]
            if b in d and b not in c:
                a.append(b)
                c.add(b)
            else:
                d.add(b)
        return a
   
