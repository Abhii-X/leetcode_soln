'''
Example 1:
Input: nums1 = [2,3]
Output: true
Explanation:
Choose nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1.
Choose nums2[1] = nums1[1] = 3.
nums2 = [-1, 3], and both elements are odd. Thus, the answer is true​​​​​​​.
Example 2:
Input: nums1 = [4,6]
Output: true
Explanation:​​​​​​​
Choose nums2[0] = nums1[0] = 4.
Choose nums2[1] = nums1[1] = 6.
nums2 = [4, 6], and all elements are even. Thus, the answer is true.'''
Link:https://leetcode.com/problems/construct-uniform-parity-array-i/description/?envType=daily-question&envId=2026-09-02
#code:
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        a = []
        n = len(nums1)

        for i in range(n):
            for j in range(n):
                if i != j:
                    a.append(nums1[i] - nums1[j])
                else:
                    a.append(nums1[i])

        print(a)
        e = False
        o = False
        for val in a:
            if val % 2 == 0:
                e = True
            else:
                o = True
        return e or o
