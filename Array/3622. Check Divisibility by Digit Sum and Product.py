'''
Example:
Input: n = 99

Output: true

Explanation:

Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.'''
#Link:https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description/?envType=daily-question&envId=2026-08-22
#  Code:
class Solution:
    def checkDivisibility(self, n: int) -> bool:

        x=n
        s=0
        a=n

        while a>0:
            b=a%10
            s+=b
            a//=10

        p=1

        while n>0:
            b=n%10
            p=p*b
            n=n//10

        c=s+p

        if x%c==0:
            return True
        else:
            return False
