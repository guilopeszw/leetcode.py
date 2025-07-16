from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Counter_s = Counter(s)
        Counter_t = Counter(t)
        if Counter_s != Counter_t:
            return False
        return True