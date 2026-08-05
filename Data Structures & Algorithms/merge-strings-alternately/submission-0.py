class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        n=min(len(word1),len(word2))
        for i in range(n):
            res+=word1[i]
            res+=word2[i]
        x,y=n,n
        while x<len(word1):
            res+=word1[x]
            x+=1
        while y<len(word2):
            res+=word2[y]
            y+=1
        return res