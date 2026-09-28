'''
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4'''

#Link:https://leetcode.com/problems/search-insert-position/description/

#Code

        i=0
        j=len(nums)-1
        while i<=j:
            mid=i+((j-i)//2)
            if target<nums[mid]:
                j=mid-1
            else:
                i=mid+1
        return i if target not in nums else i-1
