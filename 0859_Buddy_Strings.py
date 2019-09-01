# Problem 859 
# Date completed: 2019/09/01

# 28 ms
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        len_A = len(A)
        diff_A = None
        diff_B = None
        swaped = False
        
        if len_A != len(B):
            return False
        
        if A == B:
            return len(set(A)) < len_A
        
        for i in range(len(A)):   
            if A[i] != B[i]:
                if diff_A:
                    if swaped:
                        return False
                    else:
                        if A[i] == diff_B and B[i] == diff_A:
                            swaped = True
                        else:
                            return False
                else:
                    diff_A, diff_B = A[i], B[i]
        
        return swaped
            
