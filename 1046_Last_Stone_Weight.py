# Problem 1046
# Date completed: 2020/04/12 

# 28 ms (%)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        counts = collections.Counter(stones)
        keys = sorted(counts.keys())
        
        def insert_key(keys,new_key):
            # print('Insert key', new_key, keys)
            # Binary should be faster but here the array is short
            if not keys:
                return [new_key]
            elif new_key < keys[0]:
                return [new_key]+keys
            elif new_key > keys[-1]:
                return keys + [new_key]
            else:
                for i in range(len(keys)):
                    if keys[i] > new_key:
                        return keys[:i] + [new_key] + keys[i:]
        
        while keys:
            
            key = keys.pop()
            if counts[key] % 2 == 1:
                
                if keys:
                    next_key = keys[-1]
                else:
                    return key
                
                counts[key] = 0 
                counts[next_key] -= 1                
                  
                diff = key-next_key
                if counts[next_key] == 0 and diff != next_key:
                    keys.pop()  
                    
                if diff in counts:
                    counts[diff] += 1
                    if diff > next_key: keys.append(diff)
                else:
                    counts[diff] = 1
                    keys = insert_key(keys,diff)
            else:
                counts[key] = 0
                
            
        return 0
            
            
