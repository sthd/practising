import collections
from typing import List


# group anagrams into a list ## runtime beats 89%, memory beats 95%
# from typing import List
def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in groups:
            groups[sorted_word].append(word)
        else:
            groups[sorted_word] = [word]
    return list(groups.values())



# lru cache ## runtime beats 80%, memory beats 99%
#import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.limit = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.limit:
            self.cache.popitem(last = False)



def compress(chars: List[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
        letter = chars[i]
        count = 0
        while i < len(chars) and chars[i] == letter:
            count += 1
            i += 1
        chars[ans] = letter
        ans += 1
        if count > 1:
            for c in str(count):
                chars[ans] = c
                ans += 1

    return ans


if __name__ == '__main__':
    list1 = ["eat", "", " ", "  ", "tea", "tan", "ate", "nat", "bat", ""]
    chars = ["a", "a", "c", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "a"]
    chars = ["a", "a", "c", "b", "b", "b"]

    print(compress(chars))