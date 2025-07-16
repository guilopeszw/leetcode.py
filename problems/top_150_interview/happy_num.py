class Solution:
    def isHappy(self, n: int) -> bool:
        str_num = str(n)
        seen = set()
        while str_num not in seen:
            seen.add(str_num)
            total = sum(int(digit) ** 2 for digit in str_num)
            str_num = str(total)
        return False if str_num != '1' else True