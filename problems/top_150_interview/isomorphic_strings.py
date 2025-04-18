class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h_st = {}
        h_ts = {}

        for i in range(len(s)):
            char1, char2 = s[i], t[i]

            if (((char1 in h_st) and (h_st[char1] != char2))
                    or ((char2 in h_ts) and (h_ts[char2] != char1))):
                return False

            h_st[char1] = char2
            h_ts[char2] = char1
        return True
