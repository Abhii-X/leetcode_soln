'''
Example:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".'''
#Link:https://leetcode.com/problems/reverse-prefix-of-word/description/
#Code:
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l=[]
        if ch not in word:
            return word
        else:
            for i in range(len(word)):
                if ch==word[i]:
                    l.append(word[i])
                    k=i+1
                    break
                else:
                    l.append(word[i])
            r=""
            for i in range(len(l)):
                r+=l.pop()
            r+=word[k:]
            return r
