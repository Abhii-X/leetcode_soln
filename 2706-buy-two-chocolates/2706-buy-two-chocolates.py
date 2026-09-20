class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        '''c=max(prices)
        b=[]
        for i in prices:
            if i==c:
                continue
            else:
                b.append(i)
        d=max(b)
        if c+d>money:
            return money
        else:
            return (c+d)-money'''


        a=sorted(prices)
        print(*a)
        if a[0]+a[1]>money:
            return money
        else:
            return money-(a[0]+a[1])