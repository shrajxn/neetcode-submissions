import heapq  
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1={}
        for num in nums:
            if num not in hash1:
                hash1[num]=1
            else:
                hash1[num]+=1
        min_heap=[]

        for num,freq in hash1.items():
            heapq.heappush(min_heap,(freq,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [item[1] for item in min_heap]

