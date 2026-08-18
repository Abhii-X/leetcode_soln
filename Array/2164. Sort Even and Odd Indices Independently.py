'''
Example:
Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation: 
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,1,2,3] to [4,3,2,1].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [4,1,2,3] to [2,3,4,1].
Thus, the array formed after rearranging the values is [2,3,4,1].'''
#Link:https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/
#Code:
class Solution:
    def sortEvenOdd(self, nums):
        a=[]
        b=[]
        for i in range(len(nums)):
            if i%2==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        a.sort()
        b.sort(reverse=True)
        print(a)
        print(b)
        c=0
        d=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=a[c]
                c+=1
            else:
                nums[i]=b[d]
                d+=1
        return nums
