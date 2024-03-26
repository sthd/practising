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



# group anagrams into a list ## runtime beats 80%, memory beats 99%
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


if __name__ == '__main__':
    list1 = ["eat", "", " ", "  ", "tea", "tan", "ate", "nat", "bat", ""]
    chars = ["a", "a", "c", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "a"]
    chars = ["a", "a", "c", "b", "b", "b", "xx"]

    last_char = None
    group_size = 1
    index = 0
    while index < len(chars):
        if chars[index] == last_char:
            group_size += 1
            chars.pop(index)
            index -=1
        else:
            if 1 < group_size:
                chars.insert(index, group_size)
            group_size = 1

        last_char = chars[index]
        index += 1
    print(chars)
    chars.pop(len(chars) -1 )
    print(chars)
    print((len(chars)))
    # print(group_anagrams(list1))
    # capacity = 3
    # obj = LRUCache(capacity)
    # param_1 = obj.get(3)
    # print(f"param 1: {param_1}")
    # obj.put(1, "one")
    # param_1 = obj.get(1)
    # print(f"param 1: {param_1}")
    # obj.put(2, "two")
    # param_1 = obj.get(3)
    # print(f"param 1: {param_1}")
    # obj.put(3, "three")
    # param_1 = obj.get(3)
    # print(f"param 1: {param_1}")
    # obj.put(1, "one ")
    # param_1 = obj.get(1)
    # print(f"param 1: {param_1}")
    # obj.put(32, "fourth")
    # param_1 = obj.get(1)
    # print(f"param 1: {param_1}")
    # param_1 = obj.get(32)
    # print(f"param 1: {param_1}")
    # print(f"param 1: {param_1}")

    chars.insert(index, str(group_size // 10))
    group_size %= 10
    index += 1