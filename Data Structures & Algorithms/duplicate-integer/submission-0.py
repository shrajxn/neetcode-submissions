class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array=[]
        for num in nums:
            if num not in array:
                array.append(num)
            else:
                return True
        return False
         