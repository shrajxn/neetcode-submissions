class Solution:
    def isPalindrome(self, s: str) -> bool:
        w="".join(char.lower() for char in s if char.isalnum())
        L,R=0,len(w)-1
        while L<R:
            if w[L]!=w[R]:
                return False
            R-=1
            L+=1
        return True