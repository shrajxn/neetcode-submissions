class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))   # FIX 1
            else:
                b = stack.pop()            # val1
                a = stack.pop()            # val2

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)    # FIX 2
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))  # FIX 3

        return stack[-1]
