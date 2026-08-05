class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash1={}
        length=(len(nums)/3)
        result=[]
        for num in nums:
            if num in hash1:
                hash1[num]+=1
            else:
                hash1[num]=1
        result=[]
        for k,v in hash1.items():
            if v>length:
                result.append(k)
        return result