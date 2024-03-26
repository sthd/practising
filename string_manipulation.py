# runtime beats 67%, memory beats 53%
def merge_strings_alternately(word1: str, word2: str) -> str:
    merged = ''
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            merged += word1[i]
        if i < len(word2):
            merged += word2[i]
        i += 1
    return merged


# runtime beats 88%, memory beats 93.64%
def merge_strings_alternately2(word1: str, word2: str) -> str:
    """
            :type word1: str
            :type word2: str
            :rtype: str
            """
    result = []
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1
    return ''.join(result)


# reverse words in string ## runtime beats 75%, memory beats 80%
def reverse_order_of_words(s: str) -> str:
    return " ".join(reversed(s.split()))


# reverse words in string ## runtime beats 82%, memory beats 80%
def reverse_order_of_words2(s: str) -> str:
    return " ".join((s.split())[::-1])


# Reverse Vowels of a String ## runtime beats 88%, memory beats 88%
def reverse_vowels_order_in_string(s: str) -> str:
    s = list(s)
    left = 0
    right = len(s) - 1
    m = 'aeiouAEIOU'
    while left < right:
        if s[left] in m and s[right] in m:

            s[left], s[right] = s[right], s[left]

            left += 1;
            right -= 1

        elif s[left] not in m:
            left += 1

        elif s[right] not in m:
            right -= 1

    return ''.join(s)


# Reverse Vowels of a String ## runtime beats 99%, memory beats 51%
def reverse_vowels_order_in_string2(s: str) -> str:
    s=list(s)
    n=len(s)
    left=0
    right=n-1
    vowels=set('AEIOUaeiou')
    while left<right:
        while left<right and s[left] not in vowels:
            left+=1
        while left<right and s[right] not in vowels:
            right-=1
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    s=''.join(s)
    return s

# ## runtime beats 97%, memory beats 81%
def remove_chars_ands_stars(s: str) -> str:
    stack = []
    for i in s:
        if i == '*':
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)

# ## runtime beats 76%, memory beats 61% # if it is possible to receive a string where num_other_chars < num_of_stars
def remove_chars_ands_stars2(s: str) -> str:
    res = []
    for i in s:
        if i != '*':
            res.append(i)
        elif res:
            res.pop()
    return ''.join(res)


if __name__ == '__main__':
    str1 = "idkfa"
    str2 = "clapiucius"
    str3 = "do not worry about a thing"
    print(f"merged is: {merge_strings_alternately2(str1, str2)}")
    print(f"reversed order of words is: {reverse_order_of_words(str3)}")
    print(reverse_vowels_order_in_string("eo"))