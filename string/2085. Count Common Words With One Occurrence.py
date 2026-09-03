'''
Example :
Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.'''

#Link:https://leetcode.com/problems/count-common-words-with-one-occurrence/description/

#Code:
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a=[]
        for i in words1:
            for j in words2:
                if i==j and words1.count(i)==1 and words2.count(j)==1:
                    a.append(i)
        return len(a)
