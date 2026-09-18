class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l=list(ransomNote)
        k=list(magazine)
        c=0
        for i in l:
            if i in k:
                c+=1
                k.remove(i)
        return len(l)==c