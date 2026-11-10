'''

Example 1:

Input: num = 4, t = 1

Output: 6

Explanation:

Apply the following operation once to make the maximum achievable number equal to num:

Decrease the maximum achievable number by 1, and increase num by 1.
Example 2:

Input: num = 3, t = 2

Output: 7

Explanation:

Apply the following operation twice to make the maximum achievable number equal to num:

Decrease the maximum achievable number by 1, and increase num by 1.'''


Link:https://leetcode.com/problems/find-the-maximum-achievable-number/description/

#Code:

class Solution {
public:
    int theMaximumAchievableX(int num, int t) {
        return num+(2*t);
    }
};
