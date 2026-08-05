class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char not in ['/','+','-','*']:
                stack.append(int(char))
            else:
                val1=stack.pop()
                val2=stack.pop()
                if char=='+':
                    stack.append(val1+val2)
                elif char=='-':
                    stack.append(val2-val1)
                elif char=='*':
                    stack.append(val1*val2)
                else:
                    stack.append(int(val2/val1))
        return stack[-1]