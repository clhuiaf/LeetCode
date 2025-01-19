class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        open_to_close = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in open_to_close:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if c != open_to_close[top]:
                        return False
        return not stack