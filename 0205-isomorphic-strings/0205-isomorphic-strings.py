class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        a1=[]
        a2=[]
        for i in range(len(s)):
            a1.append(s.index(s[i]))
            a2.append(t.index(t[i]))
        
        if a1==a2:
            return True
            
        return False

            



        
