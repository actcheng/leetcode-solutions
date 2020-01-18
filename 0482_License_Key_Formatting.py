# Problem 482
# Date completed: 2020/01/18 

# 28 ms (98%)
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        text = ''.join(S.split('-')).upper()
        groups, first = len(text)//K, len(text)%K
        return '-'.join(([text[:first]] if first>0 else []) + [text[first+n*K:first+(n+1)*K] for n in range(groups)])
