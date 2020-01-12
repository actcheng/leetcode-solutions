# Problem 937
# Date completed: 2020/01/12 

# 36 ms (53%)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        let = collections.defaultdict(list)
        digits=set('1234567890')
        for log in logs:
            words = log.split()
            if words[1][0] in digits: # Num
                dig.append(log)
            else:
                word = ' '.join(words[1:])
                let[word].append(log)
        
        keys = sorted(let.keys())
        let_list = []
        for key in keys:
            let_list.extend(sorted(let[key]))

        return let_list + dig
