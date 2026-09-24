class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        x=-1
        for i in range(len(nums)):
            s=0
            while nums[i]>0:
                l=nums[i]%10
                s+=l
                nums[i]//=10
            if s==i:
                x=i
                break
        return x