from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res
        
    def decode(self, s: str) -> List[str]:
        # ["leet","code"]
        # "4#leet4#code"
        res = []
        i = 0
        while i != len(s):
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            res.append(s[i+1:i+int(length)+1])
            i += int(length) + 1
        return res
            

