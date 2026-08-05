class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash1={}
        for i,num in enumerate(nums):
            if num in hash1 and abs(hash1[num]-i)<=k:
                return True
            hash1[num]=i
        return False