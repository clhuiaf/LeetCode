class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ""
        b = ""
        for c in s:
            c_lower = c.lower()
            if (c_lower >= 'a' and c_lower <= 'z') or \
                (c_lower >= '0' and c_lower <= '9') :
                f += c_lower
        for c in s[::-1]:
            c_lower = c.lower()
            if (c_lower >= 'a' and c_lower <= 'z') or \
                (c_lower >= '0' and c_lower <= '9') :
                b += c_lower
        if f == b:
            return True
        return False
        
