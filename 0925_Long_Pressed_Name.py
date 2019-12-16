# Problem 925
# Date completed: 2019/12/16 

# 24 ms (94%)
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # 'x' -> 'x', xx', 'xx' -> 'xx', 'xxx'... -> True
        # 'x' -> '', 'xx' -> 'x', '' -> False -> return immediately
        l = len(name)
        i = 0
        p = None
        for c in typed:
            if i < l and c == name[i]:
                p = name[i]
                i += 1
            elif c != p:
                return False
        return i == l
