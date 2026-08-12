class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(num):
            mid=len(num)//2
            if len(num)<=1:
                return num
            left=divide(num[:mid])
            right=divide(num[mid:])
            return merge(left,right)
        def merge(left,right):
            ans=[]
            i,j=0,0
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    ans.append(left[i])
                    i+=1
                else:
                    ans.append(right[j])
                    j+=1
            while i<len(left):
                ans.append(left[i])
                i+=1
            while j<len(right):
                ans.append(right[j])
                j+=1
            return ans
        return divide(nums)

            