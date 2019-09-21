# Problem 599
# Date completed: 2019/09/21

# 268 ms
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indSum = {}
        for x in set(list1).intersection(set(list2)):
            sum = list1.index(x)+list2.index(x)
            if sum in indSum:
                indSum[sum].append(x)
            else:
                indSum[sum] = [x]
        return indSum[min(indSum)]
