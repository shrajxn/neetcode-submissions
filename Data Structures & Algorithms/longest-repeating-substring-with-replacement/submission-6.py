class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        maxfreq=0
        res=0
        for right in range(len(s)):
            char=s[right]
            if char in count:
                count[char]+=1
            else:
                count[char]=1
            maxfreq=max(maxfreq,count[char])
            while (right-left+1) - maxfreq >k:
                count[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res
            


    
