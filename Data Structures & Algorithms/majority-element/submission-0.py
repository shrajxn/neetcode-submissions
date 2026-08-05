class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash1={}
        for num in nums:
            if num in hash1:
                hash1[num]+=1
            else:
                hash1[num]=1
        val= max(hash1,key=hash1.get)
        return val
      