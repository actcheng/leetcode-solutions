# Problem 697
# Date completed: 2019/12/18 

# 260 ms (74%)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = {}
        ind = {}
        degree = 0        
        for i in range(len(nums)):
            num = nums[i]
            if num in counts:
                counts[num] += 1    
                ind[num][1] = i
            else:
                counts[num] = 1
                ind[num] = [i,i]
                
            if counts[num]>degree: 
                degree = counts[num]
                freq_num = [num]
            elif counts[num]==degree:
                freq_num.append(num)
        
        return min(ind[num][1]-ind[num][0]+1 for num in freq_num)
