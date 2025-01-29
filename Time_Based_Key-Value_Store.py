from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.pairs = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairs[key].append([value, timestamp])
            

    def get(self, key: str, timestamp: int) -> str:
        values = self.pairs[key]
        start, end = 0, len(values)-1
        result = ""
        while start <= end:
            mid = start + (end-start)//2
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                start = mid + 1
            else:
                end = mid - 1
        return result 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)