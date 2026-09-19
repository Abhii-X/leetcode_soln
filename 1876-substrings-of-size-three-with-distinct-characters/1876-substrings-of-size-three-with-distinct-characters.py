class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        a=0
        for i in range(n-2):
            if s[i]!=s[i+1] and s[i]!=s[i+2] and s[i+1]!=s[i+2]:
                a+=1
        return a