class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        big=0
        for num in nums:
            if num>big:
                big=num
        for i in range(1,big):
            if i not in nums:
                return i
        return big+1
            
        
