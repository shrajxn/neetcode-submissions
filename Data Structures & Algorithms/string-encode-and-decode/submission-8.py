class Solution:
    def encode(self, strs: List[str]) -> str:
        res=''
        for word in strs:
            res+=(word)
            res+=('~')
        return res
    def decode(self, s: str) -> List[str]:
        word=''
        res=[]
        for char in s:
            if char!='~':
                word+=(char)
            else:
                res.append(word)
                word=''
        return res


        
