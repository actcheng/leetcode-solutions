# Problem 811 
# Date completed: 2019/09/16

# 64 ms
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for cp in cpdomains:
            count = int(cp.split()[0])
            splits = cp.split()[1].split('.')
            splits.reverse()
            subdomain = None
            for s in splits:
                if not subdomain: 
                    subdomain = s
                else:
                    subdomain = s+'.'+subdomain
                if subdomain not in counts:
                    counts[subdomain] = count
                else:
                    counts[subdomain] += count
        return ['{} {}'.format(counts[key],key) for key in counts]
