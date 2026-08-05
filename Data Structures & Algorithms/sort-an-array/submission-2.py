class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Merge sort
        def merge(left,right):
            res=[]
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left_half=self.sortArray(nums[:mid])
        right_half=self.sortArray(nums[mid:])
        return merge(left_half,right_half)
    
