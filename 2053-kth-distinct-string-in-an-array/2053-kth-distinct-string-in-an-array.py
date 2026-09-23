class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        a=[]
        for i in arr:
            if arr.count(i)==1:
                a.append(i)
        if len(a)>=k:
            return a[k-1]
        else:
            return ""