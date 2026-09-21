class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word2)
        m=len(word1)
        leng=min(m,n)
        i=0
        res=''
        while i<leng:
            res+=word1[i]
            res+=word2[i]
            i+=1
        res+=word1[i:]
        res+=word2[i:]
        return res
