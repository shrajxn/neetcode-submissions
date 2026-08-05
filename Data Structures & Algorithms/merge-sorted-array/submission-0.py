class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        combined = nums1[:m] + nums2[:n]

        def merge(arr,l,r,m):
            left=arr[l:m+1]
            right=arr[m+1:r+1]
            i,j,k=l,0,0
            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    arr[i]=left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j<len(left):
                arr[i]=left[j]
                j+=1
                i+=1
            while k<len(right):
                arr[i]=right[k]
                k+=1
                i+=1
            
        def divide(arr,l,r):
            if l==r:
                return arr
            m=(l+r)//2
            divide(arr,l,m)
            divide(arr,m+1,r)
            merge(arr,l,r,m)
            return arr
        divide(combined,0,len(nums1)-1)
        for i in range(len(combined)):
            nums1[i] = combined[i]
        