"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Brute Force
# T.C.->O(n^2)
# S.C.->O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        for i in range(n):
            A = intervals[i]
            for j in range(i + 1, n):
                B = intervals[j]
                if min(A.end, B.end) > max(A.start, B.start):
                    return False
        return True


# Sorting
#T.C.->O(nlogn)
# S.C.->O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True
