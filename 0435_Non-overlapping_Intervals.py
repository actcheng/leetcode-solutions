# Problem 435
# Date completed: 2020/08/16

# 88 ms (29%)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        
        ends = {}
        for start, end in intervals:
            if start not in ends or end < ends[start]:
                ends[start] = end
            
        starts = sorted(ends.keys())
        
        counts = 1
        prev_end = ends[starts[0]]
        for start in starts[1:]:
            if start >= prev_end:
                counts += 1
                prev_end = ends[start]
            elif ends[start] < prev_end:
                prev_end = ends[start]

        return len(intervals) - counts

