class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                L,R=j+1,n-1
                while L<R:
                    total=nums[i]+nums[j]+nums[L]+nums[R]
                    if total==target:
                        result.append([nums[i],nums[j],nums[L],nums[R]])
                        L+=1
                        R-=1
                        while L<R and nums[L]==nums[L-1]:
                            L+=1
                        while L<R and nums[R]==nums[R+1]:
                            R-=1
                    elif total<target:
                        L+=1
                    else:
                        R-=1
        return result

