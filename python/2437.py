class Solution:
    def countTime(self, time: str) -> int:
        ans = 1
        # h
        if time[0] == '?' and time[1] == '?':
            ans *= 24
        elif time[0] == '?':
            if int(time[1] < 4): 
                ans *= 3
            else:
                ans *= 2
        elif time[1] == '?':
            if int(time[0]) < 2:
                ans *= 10
            else:
                ans *= 4
        # m
        if time[3] == '?':
            ans *= 6
        if time[4] == '?':
            ans *= 10
        return ans 