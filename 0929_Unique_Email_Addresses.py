# Problem 929
# Date completed: 2020/01/14 

# 64 ms (24%)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            real_local=''
            for l in local:
                if l == '+':
                    break
                elif l!='.':
                    real_local += l
            print(f'{real_local}@{domain}')
            unique.add(f'{real_local}@{domain}')
        return len(unique)
