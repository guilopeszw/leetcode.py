class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        n1 = len(word1)
        n2 = len(word2)
        for i in range(max(n1, n2)):
            if i < n1:
                merged += word1[i]
            if i < n2:
                merged += word2[i]
        return merged