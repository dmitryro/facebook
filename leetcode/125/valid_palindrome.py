import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        s = s.lower()
        for i in s:
            if re.search('[a-zA-Z0-9]', i):
                res.append(i)
        c = ''.join(res)
        if c == c[::-1]:
            return True
        return False
