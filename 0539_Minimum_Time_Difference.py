# Problem 539
# Date completed: 2019/10/11

# 84 ms (80%)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(time.split(':')[0])*60+int(time.split(':')[1]) for time in timePoints]
        minutes.sort()
        minutes.append(minutes[0]+1440)
        diff = [minutes[i+1] - minutes[i] for i in range(len(minutes)-1)]
        return min(diff)
