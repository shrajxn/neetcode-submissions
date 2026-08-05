class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            j=i+1
            k=n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                cursum=nums[i]+nums[j]+nums[k]
                if cursum>0:
                    k-=1
                elif cursum<0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                    
        return res
