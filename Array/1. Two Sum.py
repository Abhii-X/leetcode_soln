'''1. Two Sum
""Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''
#code link: https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,j in enumerate(nums):
            if target-j in d:
                return [d[target-j],i]
            d[j]=i
