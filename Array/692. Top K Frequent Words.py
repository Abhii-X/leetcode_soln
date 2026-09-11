'''
Example
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.'''

#Link:https://leetcode.com/problems/top-k-frequent-words/description/

#Code:
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        b=[]
        f={}
        for i in words:
            f[i]=f.get(i,0)+1
        a=sorted(f.items(),key=lambda x:(-x[1],x[0]))
        for i in range(k):
            b.append(a[i][0])
        return b
