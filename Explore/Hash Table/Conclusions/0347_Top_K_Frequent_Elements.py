# Problem 347
# Date completed: 2019/09/27 

# 120 ms
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        topK = set(sorted(counts.values(),reverse=True)[:k])
        return [key for key in counts if counts[key] in topK]
