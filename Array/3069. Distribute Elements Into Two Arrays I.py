'''
Example:
Input: nums = [5,4,3,8]
Output: [5,3,4,8]
Explanation: After the first 2 operations, arr1 = [5] and arr2 = [4].
In the 3rd operation, as the last element of arr1 is greater than the last element of arr2 (5 > 4), append nums[3] to arr1, hence arr1 becomes [5,3].
In the 4th operation, as the last element of arr2 is greater than the last element of arr1 (4 > 3), append nums[4] to arr2, hence arr2 becomes [4,8].
After 4 operations, arr1 = [5,3] and arr2 = [4,8].
Hence, the array result formed by concatenation is [5,3,4,8].'''
#Link:https://leetcode.com/problems/distribute-elements-into-two-arrays-i/description/?envType=daily-question&envId=2026-08-20
#Code:
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a=[nums[0]]
        b=[nums[1]]
        for i in range(2,len(nums)):
            if a[-1]>b[-1]:
                a.append(nums[i])
            else:
                b.append(nums[i])
        return a+b
