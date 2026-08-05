class Solution:
    def encode(self, strs: List[str]) -> str:
        res=""
        for num in strs:
            res+=num
            res+="?"
        return res
    def decode(self, s: str) -> List[str]:
        result=[]
        current_word=""
        for char in s:
            if char=="?":
                result.append(current_word)
                current_word=""
                continue
            current_word+=char
        return result
