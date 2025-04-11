class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s)

        if s.lower() == s[::-1].lower():
            return True
        else:
            return False