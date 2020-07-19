# Problem 1344
# Date completed: 2020/07/12 

# 48 ms (32%)
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        ang_hr = (hour + minutes/60)/12 * 360
        ang_min = minutes / 60 *360
        diff = abs(ang_hr - ang_min)
        return min(diff,360-diff)
