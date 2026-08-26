'''Example:
Input: nums = [0,1,0,3,12]

Output: 2

Explanation:

We perform the following swap operations:

Swap nums[0] and nums[3], giving nums = [3, 1, 0, 0, 12].
Swap nums[2] and nums[4], giving nums = [3, 1, 12, 0, 0].
Thus, the answer is 2.'''
#Link:https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/description/
#Code:
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        i=0
        j=len(nums)-1
        count=0
        while i<j:
            if nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                count+=1
            elif nums[j]==0:
                j-=1
            else:
                i+=1
        print(count)
        return count
