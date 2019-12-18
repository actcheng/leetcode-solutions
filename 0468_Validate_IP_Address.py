# Problem 468
# Date completed: 2019/12/18 

# 16 ms (99.8%)
class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        def checkIPv4(IP):
            nums = IP.split('.')
            if len(nums) != 4: return False
            for num in nums:
                try:
                    i = int(num)
                    if i>255 or i<0 or (len(num)>1 and int(num[0])==0): 
                        return False
                except:
                    return False
            return True
        
        def checkIPv6(IP):
            nums = IP.split(':')
            if len(nums) != 8: return False
            for num in nums:
                if not (0<len(num)<=4): return False
                try:
                    i = int(num,16)
                    if i<0 or num[0] == '-': return False
                except:
                    return False
            return True
                
        if ':' in IP and checkIPv6(IP):
            return "IPv6"
        elif checkIPv4(IP):
            return "IPv4"
        else:
            return "Neither"
