class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        print(f)
        for i,j in f.items():
            if j>len(nums)//2:
                return i