# Sorting and Heap
# T.C.->O(nlogn)
# S.C.->O(n)
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  # Sort by start day
        n = len(events)
        min_heap = []  # Acts as a min-heap for end days
        day = events[0][0]
        i = 0
        count = 0

        while min_heap or i < n:
            # Add all events starting today
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # Attend one event today
            if min_heap:
                heapq.heappop(min_heap)
                count += 1

            day += 1

            # Remove events whose end day has passed
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

        return count
