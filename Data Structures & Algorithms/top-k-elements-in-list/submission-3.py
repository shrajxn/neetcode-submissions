import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1 
        heap=[]
        for num,values in hashmap.items():
            heapq.heappush(heap,(values,num))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for value,num in heap:
            res.append(num)
        return res
            

        
        
        