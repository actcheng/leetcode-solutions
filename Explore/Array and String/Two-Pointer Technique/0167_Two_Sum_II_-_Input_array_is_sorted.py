# Problem 167
# Date completed: 2019/09/28 

# 76 ms
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        sum = numbers[i]+numbers[j]
        while sum != target:
            if sum > target: 
                j -=1
            else:
                i +=1
            sum = numbers[i]+numbers[j]
            # print(i,j,sum)
        return [i+1,j+1]
