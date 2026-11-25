'''

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
Sorting them in non-increasing order of frequency and placing them back into the vowel positions results in "aaaaoooiie".
Example 3:

Input: s = "baeiou"

Output: "baeiou"

Explanation:

Each vowel appears exactly once, so all have the same frequency.
Thus, they retain their relative order based on first occurrence, and the string remains unchanged.'''

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
