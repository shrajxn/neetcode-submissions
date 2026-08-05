class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash1={}
        for i,num in enumerate(nums):
            compliment=target-num
            if compliment in hash1:
                return [hash1[compliment],i]
            hash1[num]=i
        return []

