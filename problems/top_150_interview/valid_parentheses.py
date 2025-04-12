class Solution:
    def isValid(self, s: str) -> bool:
        h = {'(': ')', '[': ']', '{': '}'}
        i = 0
        stack = []

        for i in range(len(s)):
            if s[i] in h:
                stack.append(s[i])
            if s[i] in h.values():
                if len(stack) == 0:
                    return False
                elif s[i] == h[stack[-1]]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        return False