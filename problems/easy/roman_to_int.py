class Solution(object):
    def romanToInt(self, s):
        r = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s) - 1):
            if i + 1 < len(s) and r[s[i]] < r[s[i + 1]]:
                result -= r[s[i]]
            else:
                result += r[s[i]]

        return result + r[s[-1]]