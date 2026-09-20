class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a=min(prices)
        prices.remove(a)
        b=min(prices)
        print(a,b)
        return money if a+b>money else (money-(a+b))


        '''a=sorted(prices)
        print(*a)
        if a[0]+a[1]>money:
            return money
        else:
            return money-(a[0]+a[1])'''