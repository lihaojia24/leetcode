from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def s2n(time: str) -> int:
            times = time.split(':')
            return int(times[0])*60 + int(times[1])
        time1, time2, time3, time4 = s2n(event1[0]), s2n(event1[1]), s2n(event2[0]), s2n(event2[1])
        return not (time1 > time4 or time3 > time2)

s = Solution()
event1 = ["01:15", "02:00"]
event2 = ["02:00", "03:00"]
print(s.haveConflict(event1, event2))