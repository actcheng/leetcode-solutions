# Problem 621
# Date completed: 2020/07/28

# 680 ms (29%)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        max_num = counts.most_common()[0][1]
        max_count = list(counts.values()).count(max_num)
        
        return max([(n+1)*(max_num-1)+max_count, len(tasks)])
