class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        

# => 1st method
        # s=s.split(" ")
        # return len(s[-1])

# => 2nd method  
        n=len(s)
        i=-1
        while i>=(-1*n) and s[i]!=" ":
            i-=1
        i+=1
        return i*(-1)
