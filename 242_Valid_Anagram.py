def isAnagram(self, s: str, t: str) -> bool:
    hashmap_s = {char:s.count(char) for char in s } 
    hashmap_t = {char:t.count(char) for char in t } 
    if (hashmap_s == hashmap_t):
        return True
    return False