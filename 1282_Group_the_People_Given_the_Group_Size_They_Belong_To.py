# Problem 1282
# Date completed: 2019/12/21 

# 72 ms (93%)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i,n in enumerate(groupSizes):
            if n in groups:
                if len(groups[n][-1]) == n:
                    groups[n].append([i])
                else:
                    groups[n][-1].append(i)
            else:
                groups[n] = [[i]]
        res = []
        for n in groups:
            res.extend(groups[n])
        return res
