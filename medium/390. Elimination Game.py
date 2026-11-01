'''
You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Given the integer n, return the last number that remains in arr.

 

Example 1:

Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]
Example 2:

Input: n = 1
Output: 1'''

#Code:

class Solution:
    def lastRemaining(self, n: int) -> int:
        if n==1:
            return 1
        '''def game(a,i):
            if len(a)==1:
                return a[0]
            if i%2==0:
                for j in range(len(a)-1,-1,-1):
                    if j%2==0:
                        a.pop(j)
        
            else:
                for j in range(len(a)-1,-1,-2):
                    a.pop(j)
            return game(a,i+1)


        a=[]
        for i in range(1,n+1):
            a.append(i)
        return game(a,0)'''

        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))
