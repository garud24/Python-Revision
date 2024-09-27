import math
def evalRPN(tokens):
    numStack = []
    
    num1 = 0
    num2 = 0
    tokens.reverse()
    while tokens:
        token = tokens.pop()
        res = 0
        if token not in ['+','-','*','/']:
            numStack.append(int(token))
        else:
            if token == '+':
                num1 = numStack.pop()
                num2 = numStack.pop()
                res = num1 + num2
                numStack.append(res)
                print("numStack in +", numStack)
            elif token == '-':
                num1 = numStack.pop()
                num2 = numStack.pop()
                res = num2 - num1
                numStack.append(res)
                print("numStack in-", numStack)
                
            elif token == '*':
                num1 = numStack.pop()
                num2 = numStack.pop()
                print(num1,num2)
                res = num1 * num2
                numStack.append(res)
                print("numStack in *", numStack)
                
            elif token == '/':
                num1 = numStack.pop()
                num2 = numStack.pop()
                res = num2 / num1
                numStack.append(math.trunc(res))
                print("numStack in /", numStack)
                
    return numStack.pop()  

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))              
