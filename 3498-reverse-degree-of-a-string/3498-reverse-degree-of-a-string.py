class Solution:
    def reverseDegree(self, s: str) -> int:
        b=0
        i=0
        while i<len(s):
            b+=(123-ord(s[i]))*(i+1)
            i+=1
        return b