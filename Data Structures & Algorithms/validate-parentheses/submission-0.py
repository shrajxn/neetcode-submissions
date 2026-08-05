class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack=[]
        hashmap={
            '(':')',
        '[':']',
        '{':'}'}
        for char in s:
            if char in hashmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if char!= hashmap[top]:
                    return False
        return len(stack)==0
