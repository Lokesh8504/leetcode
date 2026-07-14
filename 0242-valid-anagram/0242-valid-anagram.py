class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#method 1 =>
        # list1= list(s)
        # list2=list(t)
        # list1.sort()
        # list2.sort()
        # a="".join(list1)
        # b="".join(list2)
        # if a==b:
        #     return True
        # else:
        #     return False
        
#method 2 (dictionary or maping)=>
        # if len(s)!=len(t):
        #     return False
        # freq={}
        # for i in s:
        #     if i not in freq:
        #         freq[i]=1
        #     else:
        #         freq[i]+=1
        # for i in t:
        #     if i not in freq:
        #         return False
        #     else:
        #         freq[i]-=1
        # for i in freq.values():
        #     if  i!=0:
        #         return False
        
        # return True

# method 3 (just use sort function) which automatically gives sorted list
        if sorted(s)==sorted(t):
            return True
        else: return False

