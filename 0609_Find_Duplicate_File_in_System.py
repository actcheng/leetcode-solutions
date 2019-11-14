# Problem 609
# Date completed: 2019/11/14 

# 92 ms (93%)
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = {}
        dup = set()
        for path in paths:
            files = path.split()
            directory, files = files[0], files[1:]
            for file in files:
                [filename, content] = file[:-1].split('(')
                if content in store:
                    if content not in dup: dup.add(content)
                    store[content].append(f'{directory}/{filename}')
                else:
                    store[content] = [f'{directory}/{filename}']

        # print(dup)
        # print(store)
        return [store[content] for content in dup]
