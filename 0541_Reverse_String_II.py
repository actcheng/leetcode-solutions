# Problem 541 
# Date completed: 2019/09/20

# 40 ms
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        
        res = ''
        l = len(s)
        n = l//(2*k)
        
        for i in range(n):
            res += s[2*i*k:(2*i+1)*k][::-1] + s[(2*i+1)*k:(2*i+2)*k]
            # print(res)   

        if l-2*(n-1)*k > k: res += s[2*n*k:(2*n+1)*k][::-1]
        if l > (2*n-1)*k: res+= s[(2*n+1)*k:]
        
        return res
