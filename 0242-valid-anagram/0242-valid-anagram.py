class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1= list(s)
        list2=list(t)
        list1.sort()
        list2.sort()
        a="".join(list1)
        b="".join(list2)
        if a==b:
            return True
        else:
            return False
        
