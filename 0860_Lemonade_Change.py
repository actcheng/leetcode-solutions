# Problem 860
# Date completed: 2020/01/19 

# 164 ms (19%)
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        self.drawer = {5:0,10:0,20:0}
        
        def change_20():
            if self.drawer[10] > 0 and self.drawer[5]>0:
                self.drawer[10] -= 1
                self.drawer[5] -= 1
                return True
            elif self.drawer[5]>2:
                self.drawer[5] -= 3
                return True
            else:
                return False
        
        def change_10():
            if self.drawer[5] > 0:
                self.drawer[5] -= 1
                return True
            return False
        
        def can_change(bill):
            if bill == 5:
                return True
            elif bill == 10:
                return change_10()
            else:
                return change_20()
        
        for bill in bills:
            self.drawer[bill] += 1
            if not can_change(bill): return False
        return True
