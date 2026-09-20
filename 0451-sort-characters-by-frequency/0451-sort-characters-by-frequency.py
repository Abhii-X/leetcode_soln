class Solution:
    def frequencySort(self, s: str) -> str:
        f={}
        for i in s:
            f[i]=f.get(i,0)+1
        print(f)
        a=""
        c=dict(sorted(f.items(),key=lambda c:c[1],reverse=True))
        print(c)
        for i,j in c.items():
            a+=i*j
        return a
