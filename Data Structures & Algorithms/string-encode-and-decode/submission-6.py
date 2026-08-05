class Solution:
    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+=s
            res+='~'
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        val=''
        for char in s:
            if char== '~':
                res.append(val)
                val=''
                continue
            val+=char
        return res
