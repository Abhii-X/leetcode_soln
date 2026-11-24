'''

You are given a string s consisting of lowercase English characters.

Rearrange only the vowels in the string so that they appear in non-increasing order of their frequency.

If multiple vowels have the same frequency, order them by the position of their first occurrence in s.

Return the modified string.

Vowels are 'a', 'e', 'i', 'o', and 'u'.

The frequency of a letter is the number of times it occurs in the string.

 

Example 1:

Input: s = "leetcode"

Output: "leetcedo"

Explanation:​​​​​​​

Vowels in the string are ['e', 'e', 'o', 'e'] with frequencies: e = 3, o = 1.
Sorting in non-increasing order of frequency and placing them back into the vowel positions results in "leetcedo".
Example 2:

Input: s = "aeiaaioooa"

Output: "aaaaoooiie"

Explanation:​​​​​​​

Vowels in the string are ['a', 'e', 'i', 'a', 'a', 'i', 'o', 'o', 'o', 'a'] with frequencies: a = 4, o = 3, i = 2, e = 1.
Sorting them in non-increasing order of frequency and placing them back into the vowel positions results in "aaaaoooiie".'''


Link:https://leetcode.com/problems/sort-vowels-by-frequency/description/

#Code:

class Solution:
    def sortVowels(self, s: str) -> str:
        f={}
        for i in s:
            f[i]=f.get(i,0)+1
        a=dict(sorted(f.items(),key=lambda item: item[1],reverse=True))
        b=[]
        print(a)
        for i,j in a.items():
            if i in 'aeiou':
                b.append(i)
                b.append(j)
        print(b)
        x=""
        j=0
        for i in s:
            if i!='a' and i!='e' and i!='o' and i!='u' and i!='i':
                x+=i
            else:
                x+=b[j]
                b[j+1]-=1
                if b[j+1]==0:
                    j+=2
        return x
