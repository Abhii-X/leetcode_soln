'''
Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".'''

Link:https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/

#Code:


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        m=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                c=0
                b=s[i:j]
                for k in b:
                    if b.count(k)>2:
                        c=-1
                        break
                if c==0:
                    m=max(len(b),m)
        return m
