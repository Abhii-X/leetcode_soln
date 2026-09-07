'''
Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.'''

#Link:https://leetcode.com/problems/most-common-word/

#Code:

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        r=""
        for i in paragraph:
            if i in "'.,?""''*!;:'><":
                r+=" "
            else:
                r+=i.upper()
        k=r.split()
        c=""
        count=0
        for i in k:
            print(i)
            if k.count(i)>count and (i not in banned and i.lower() not in banned):
                c=i.lower()
                count=r.count(i)
        return c
