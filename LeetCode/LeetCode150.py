import collections
class Solution:
    def evalRPN(self, tokens) -> int:
        stack=collections.deque()
        for i in range(len(tokens)):
            if tokens[i].isdigit() or (len(tokens[i])>1 and tokens[i][0]=='-'):
                stack.append(int(tokens[i]))
            else:
                num2=stack.pop()
                num1=stack.pop()
                if tokens[i]=='+':
                    stack.append(num1+num2)
                elif tokens[i]=='-':
                    stack.append(num1-num2)
                elif tokens[i]=='/':
                    neg=-1 if num1*num2<0 else 1
                    stack.append(neg*(abs(num1)//abs(num2)))
                else:
                    stack.append(num1*num2)
        return stack.pop()
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))