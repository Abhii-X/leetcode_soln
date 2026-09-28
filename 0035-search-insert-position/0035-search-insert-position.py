class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        '''for i in nums:
            if target not in nums:
                nums.append(target)
        b=sorted(nums)
        return b.index(target)'''


        i=0
        j=len(nums)-1
        while i<=j:
            mid=i+((j-i)//2)
            if target<nums[mid]:
                j=mid-1
            else:
                i=mid+1
        return i if target not in nums else i-1