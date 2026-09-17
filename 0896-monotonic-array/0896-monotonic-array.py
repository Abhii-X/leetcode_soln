class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        a=sorted(nums)
        b=sorted(nums,reverse=True)
        if a==nums or nums==b:
            return True
        else:
            return False