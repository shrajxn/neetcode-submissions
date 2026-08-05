class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        count,res=0,0
        for num in hashset:
            if num-1 in hashset:
                continue
            count+=1
            while num+1 in hashset:
                num+=1
                count+=1
            res=max(res,count)
            count=0
        return res