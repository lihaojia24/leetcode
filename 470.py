# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

def rand7():
    return 7

class Solution:

    def rand10(self):
        """
        :rtype: int
        """
        first, second = 0, 0
        while True:
            first = rand7()
            if first < 7:
                break
        while True:
            second = rand7()
            if second < 6:
                break
        return second + 5 if first % 2 else second