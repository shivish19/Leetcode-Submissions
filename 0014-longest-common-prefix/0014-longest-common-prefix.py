class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==1:
            return strs[1]
        
        strs.sort()
        first=strs[0]
        last=strs[len(strs)-1]
        small=min(len(first),len(last))
        long_pfx=""
        for i in range(small):
            if first[i]==last[i]:
                long_pfx+=first[i]
            else: break

        return long_pfx      



        