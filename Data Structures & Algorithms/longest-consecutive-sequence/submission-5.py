class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset=set(nums)
        longest=0
        for num in numset:
            if num-1 not in numset:
                current_streak=1
                current_number=num
                while current_number+1 in numset:
                    current_streak+=1
                    current_number+=1
                longest=max(longest,current_streak)
        return longest
