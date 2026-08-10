'''Example:
Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.'''
#Link:https://leetcode.com/problems/two-out-of-three/description/
#Code:
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s=[]
        for i in nums1:
            if i in nums2 or i in nums3:
                s.append(i)
        for k in nums2:
            if k in nums1 or k in nums3 and k not in s:
                s.append(k)
        for l in nums3:
            if l in nums1 or l in nums2 and l not in s:
                s.append(l)
        d=set(s)
        return(list(d))
