class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {"+", "-", "*", "/"}
        for c in tokens:
            print(stack)
            if c not in operator:
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                if c == "+":
                    ans = a + b
                elif c == "-":
                    ans = a - b
                elif c == "*":
                    ans = a*b
                else:
                    ans = int(a / b)
                stack.append(ans)
        return stack[0]


        


            