# Problem 1170
# Date completed: 2020/01/18 

# 68 ms (88%)
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(word):
            return word.count(min(word))
        
        freq = [0]*10
        for word in words:
            freq[f(word)-1] += 1
        print(freq)
        
        for i in range(len(freq)-2,-1,-1):
            freq[i] += freq[i+1] 
        print(freq)
        
        answer = []
        store = {}
        for query in queries:
            counts = f(query)
            if counts >= len(freq):
                answer.append(0)
            else: 
                answer.append(freq[counts])
        return answer
