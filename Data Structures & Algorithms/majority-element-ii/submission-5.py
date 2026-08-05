class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        hashmap={}
        res=[]
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        for key, value in hashmap.items():
            if value>n:
                res.append(key)
        return res


