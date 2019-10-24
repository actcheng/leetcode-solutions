# Problem 150
# Date completed: 2019/10/24 

# 72 ms (95%)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        nums = []
        for token in tokens:
            if token in ["+","-","*","/"]:
                num1 = nums.pop()                
                num2 = nums.pop()
                print(num2,token,num1)
                if token == "+":
                    res = num1+num2
                elif token == "-":
                    res = num2-num1
                elif token == "*":
                    res = num1*num2
                else:
                    res = int(num2/num1)
                nums.append(res)                    
            else:
                nums.append(int(token))

        return res
