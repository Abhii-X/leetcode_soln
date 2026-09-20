class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n=c**0.5
        d=[]
        for i  in range(int(n)+1):
            d.append(i)
        print(d)
        i=0
        j=len(d)-1
        while i<=j:
            z=d[i]*d[i]+d[j]*d[j]
            if z==c:
                return True
            elif z<c:
                i+=1
            else:
                j-=1
        return False
        