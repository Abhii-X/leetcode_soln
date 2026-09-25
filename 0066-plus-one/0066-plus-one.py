class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a=""
        for i in digits:
            a+=str(i)
        a=int(a)+1
        b=[]
        for i in str(a):
            b.append(int(i))
        return b