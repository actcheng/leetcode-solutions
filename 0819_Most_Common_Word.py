# Problem 819
# Date completed: 2020/01/08 

# 36 ms (36%)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        banned = [b.lower() for b in banned]
        counts = collections.Counter(re.split(r"[!?',;. ]",paragraph.lower()))
        for key, _ in counts.most_common(len(counts)):
            if key != '' and key not in banned:
                return key
