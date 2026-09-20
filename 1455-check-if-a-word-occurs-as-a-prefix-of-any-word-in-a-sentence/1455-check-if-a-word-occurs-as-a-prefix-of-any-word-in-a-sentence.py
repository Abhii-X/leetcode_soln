class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a=list(map(str,sentence.split()))
        for i in range(len(a)):
            if a[i].startswith(searchWord):
                return i+1
                break
        return -1