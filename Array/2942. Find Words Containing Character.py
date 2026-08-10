'''Example:
Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.'''
#Link:https://leetcode.com/problems/find-words-containing-character/description/
#code:
class Solution:
    def findWordsContaining(self, words, x):
        a=[]
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j]==x:
                    a.append(i)
                    break
        return a
