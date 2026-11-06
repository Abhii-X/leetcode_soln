'''
Example 1:

Input: nums = [7,8,3,4,15,13,4,1]

Output: 5.5

Explanation:

step	nums	averages
0	[7,8,3,4,15,13,4,1]	[]
1	[7,8,3,4,13,4]	[8]
2	[7,8,4,4]	[8,8]
3	[7,4]	[8,8,6]
4	[]	[8,8,6,5.5]
The smallest element of averages, 5.5, is returned.
Example 2:

Input: nums = [1,9,8,3,10,5]

Output: 5.5

Explanation:

step	nums	averages
0	[1,9,8,3,10,5]	[]
1	[9,8,3,5]	[5.5]
2	[8,5]	[5.5,6]
3	[]	[5.5,6,6.5]
Example 3:

Input: nums = [1,2,3,7,8,9]

Output: 5.0

Explanation:

step	nums	averages
0	[1,2,3,7,8,9]	[]
1	[2,3,7,8]	[5]
2	[3,7]	[5,5]L
3	[]	[5,5,5]'''


Link:https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/

#Code

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        a=sorted(nums)
        b=[]
        i=0
        j=len(nums)-1
        while i<j:
            x=(a[i]+a[j])/2
            b.append(x)
            i+=1
            j-=1
        return min(b)
        
