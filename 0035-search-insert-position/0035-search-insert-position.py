class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in nums:
            if target not in nums:
                nums.append(target)
        b=sorted(nums)
        return b.index(target)