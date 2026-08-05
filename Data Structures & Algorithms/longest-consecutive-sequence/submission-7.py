class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        count=0
        result=0
        for num in nums:
            if num-1 in hashset:
                continue
            count+=1
            while num+1 in hashset:
                count+=1
                num=num+1
            result=max(result,count)
            count=0
        return result
