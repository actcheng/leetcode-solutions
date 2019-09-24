# Problem 56
# Date completed: 2019/09/25 

# 156 ms (slow) -> better use graph!!
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return 
        inters = []
        for interval in intervals:
            overlap = [i for i in range(len(inters)) if (interval[0] >= inters[i][0] and interval[0] <= inters[i][1]) \
                                                     or (interval[1] >= inters[i][0] and interval[1] <= inters[i][1]) \
                                                     or (inters[i][0] >= interval[0] and inters[i][0] <= interval[1]) \
                                                     or (inters[i][1] >= interval[0] and inters[i][1] <= interval[1])]
            if len(overlap) > 0:
                inters[overlap[0]][0] = min(interval[0],inters[overlap[0]][0])
                inters[overlap[0]][1] = max(interval[1],inters[overlap[0]][1])
                if len(overlap) > 1:
                    inters = self.merge(inters)
            else:
                inters.append(interval)

        return inters
