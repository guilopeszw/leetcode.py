class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split = s.split()
        if len(pattern) != len(split):
            return False
        mapping = {}
        for p, word in zip(pattern, split):
            if p in mapping:
                if mapping[p] != word:
                    return False
            else:
                if word in mapping.values():
                    return False
                mapping[p] = word
        return True