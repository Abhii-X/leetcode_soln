'''Example:
Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4. '''
#Link:https://leetcode.com/problems/count-integers-with-even-digit-sum/
#Code:
class Solution:
    def countEven(self, num: int) -> int:
        b=0
        for i in range(2,num+1):
            s=0
            while i>0:
                a=i%10
                s+=a
                i//=10
            if s%2==0 and i<=num:
                b+=1
        return b
