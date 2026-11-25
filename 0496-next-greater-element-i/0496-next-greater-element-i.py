class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n=len(nums2)
        stack=[]
        ans=[-1]*n

        hm={}
        for i in range(len(nums2)):
            hm[nums2[i]]=i
        for i in range(n-1,-1,-1):
                while (stack and stack[-1]<=nums2[i]):
                    stack.pop()
                
                if stack:
                    ans[i]=stack[-1]
                    
                stack.append(nums2[i])

        for i in range(len(nums1)):
            idx=hm[nums1[i]]
            nums1[i]=ans[idx]

        return nums1