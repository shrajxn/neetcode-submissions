class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxleft=[0]*n
        maxright=[0]*n
        maxleft[0]=height[0]
        maxright[-1]=height[-1]
        for i in range(1,n):
            maxleft[i]=max(maxleft[i-1],height[i])
        for i in range(n-2,-1,-1):
            maxright[i]=max(maxright[i+1],height[i])
        res=0
        for i in range(n):
            val=min(maxleft[i],maxright[i])-height[i]
            if val>0:
                res+=val
        return res