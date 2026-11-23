class Solution:
    def isValid(self, s: str) -> bool:
        hm={'{':'}','[':']','(':')'}
        stack=[]
        
        for char in s:
            if char in hm:
                stack.append(char)

            else:
                if not stack or hm[stack.pop()]!=char:
                    return False
        

        if not stack:
            return True
        else:
            return False
