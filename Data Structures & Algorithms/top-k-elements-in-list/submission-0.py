class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1={}
        for num in nums:
            if num not in hash1:
                hash1[num]=1
            else:
                hash1[num]+=1
        hash2=sorted(hash1,key=hash1.get,reverse=True)
        return hash2[:k]