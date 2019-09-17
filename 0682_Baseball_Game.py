# Problem 682 
# Date completed: 2019/09/17

# 40 ms
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []
        for op in ops:
            if op == "+":
                if len(points)>=2:
                    # print('2',points[-2:])
                    points.append(sum(points[-2:]))
                elif len(points)==1:
                    points.append(sum(points[-1:]))
                else:
                    points.append(0)
            elif op == "D":
                if len(points)>=1:
                    points.append(2*points[-1])
            elif op == "C":
                if len(points)>0: points.pop()
            else:
                points.append(int(op))
            # print('Points',points)
        return sum(points)
