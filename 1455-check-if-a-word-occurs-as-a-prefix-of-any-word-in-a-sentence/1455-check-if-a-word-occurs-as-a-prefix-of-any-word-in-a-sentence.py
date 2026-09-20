class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a=list(map(str,sentence.split()))
        c=-1
        for i in range(len(a)):
            if a[i].startswith(searchWord):
                c= i+1
                break
            else:
                continue
        return c