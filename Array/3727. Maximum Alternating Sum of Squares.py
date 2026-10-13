'''

Example 1:

Input: nums = [1,2,3]
Output: 12
Explanation:
A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among
all possible rearrangements.
The alternating score is calculated as:

score = 22 - 12 + 32 = 4 - 1 + 9 = 12

Example 2:
Input: nums = [1,-1,2,-2,3,-3]
Output: 16
Explanation:
A possible rearrangement for nums is [-3,-1,-2,1,3,2], which gives the maximum alternating
score among all possible rearrangements.
The alternating score is calculated as:

score = (-3)2 - (-1)2 + (-2)2 - (1)2 + (3)2 - (2)2 = 9 - 1 + 4 - 1 + 9 - 4 = 16'''

Link:https://leetcode.com/problems/maximum-alternating-sum-of-squares/description/?envType=daily-question&envId=2026-10-13
#Code:

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a,b,c,d=[],[],[],[]
        for i in nums:
            if i<0:
                a.append(abs(i))
            else:
                a.append(i)
        i,j=0,len(a)-1
        x=sorted(a)
        while i<j:
            b.append(x[i])
            c.append(x[j])
            i+=1
            j-=1
        if len(a)%2!=0:
            b.append(x[len(a)//2])
        e=sorted(b)
        f=sorted(c,reverse=True)
        m=max(len(e),len(f))
        for i in range(m):
            if i<len(f):
                d.append(f[i])
            if i<len(e):
                d.append(e[i])
        p,n,k,l=0,0,0,1
        while k<len(d):
            p+=d[k]*d[k]
            k+=2
        while l<len(d):
            n+=d[l]*d[l]
            l+=2
        return abs(p-n)
