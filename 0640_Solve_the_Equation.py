# Problem 640
# Date completed: 2019/10/16 

# 44 ms (6%)
class Solution:
    def solveEquation(self, equation: str) -> str:
        if not equation: return "Infinite solutions"
        if "=" not in equation: 
            if "x" not in equation:
                return "No solution"
            else:
                equation = equation+"=0"
        
        [left, right] = equation.split("=")
        
        def getCoefficient(side):
            side = side.replace('+',' +').replace('-',' -').split()
            res = [0, 0]
            for s in side:
                i = s.find('x')
                if i > -1:
                    try: 
                        res[1] += int(s[:i])
                    except:
                        res[1] += -1 if s[0] == '-' else 1
                else:
                    res[0] += int(s)
            return res

        coef_left, coef_right = getCoefficient(left), getCoefficient(right)
        print(coef_left,coef_right)
        if coef_left[1] == coef_right[1]: 
            if coef_left[0] == coef_right[0]:
                return 'Infinite solutions'
            return 'No solution'
        else:
            return 'x={}'.format(int((coef_left[0]-coef_right[0])/(coef_right[1]-coef_left[1])))
            
 # Sample 28 ms solution
 class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        lCoe, lConst = self.helper(left)
        rCoe, rConst = self.helper(right)
        coe = lCoe - rCoe
        const = rConst - lConst
        if coe:
            return 'x=%d' % (const / coe)
        elif const:
            return 'No solution'
        else:
            return 'Infinite solutions'
        
    def helper(self, expr):
        coe = const = 0
        num, sign = '', 1
        
        for ch in expr + '#':
            if ch.isdigit():
                num += ch
            elif ch == 'x':
                coe += int(num or '1') * sign
                num, sign = '', 1
            else:
                const += int(num or '0') * sign
                num, sign = '', 1
                if ch == '-': sign = -1
                    
        return [coe, const]
