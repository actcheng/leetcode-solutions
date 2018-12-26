class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq=[0]*n
        
        seq[0]='1'

        for i in range(n-1):
            temp =''
            count = 1
            j = 1
            num = seq[i][0]
            while j<len(seq[i]):
                if seq[i][j] == num:
                    count+=1
                    j+=1
                else:
                    temp=temp + str(count) + num
                    num = seq[i][j]
                    count = 1
                    j +=1 
            temp=temp+str(count)+num
            seq[i+1]=temp
        return seq[n-1]
                
