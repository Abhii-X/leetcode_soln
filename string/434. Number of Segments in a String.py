'''

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:

Input: s = "Hello"
Output: 1'''

Link:https://leetcode.com/problems/number-of-segments-in-a-string/description/

#Code:

class Solution:
    def countSegments(self, s: str) -> int:
      return len(list(s.split()))  
