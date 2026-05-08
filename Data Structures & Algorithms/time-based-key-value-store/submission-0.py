class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value_tuple_list = self.time_map.get(key, [])
        l, r = 0, len(value_tuple_list) - 1
        while l <= r:
            m = l + (r - l) // 2
            if value_tuple_list[m][1] <= timestamp:
                res = value_tuple_list[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
