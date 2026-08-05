import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        res=[]
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        heap=[]
        for num,val in hashmap.items():
            heapq.heappush(heap,(val,num))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for val,keyy in heap:
            res.append(keyy)
        return res