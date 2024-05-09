class Solution:
    def trailingZeroes(self, n: int) -> int:
        i=1
        count=0
        while n//pow(5,i):
            count+=n//pow(5,i)
            i+=1
        return count