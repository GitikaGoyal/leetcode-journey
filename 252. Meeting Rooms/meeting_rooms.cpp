/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

// Brute Force
// T.C.->O(n^2)
// S.C.->O(1)
class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        int n = intervals.size();
        for (int i = 0; i < n; i++) {
            Interval& A =intervals[i];
            for (int j = i + 1; j < n; j++) {
                Interval& B =intervals[j];
                if (min(A.end, B.end) > max(A.start, B.start)) {
                    return false;
                }
            }
        }
        return true;
    }
};

// Sorting
//T.C.->O(nlogn)
// S.C.->O(1)
class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), [](auto& x, auto& y) { 
            return x.start < y.start; 
        });
        for (int i = 1; i < intervals.size(); ++i) {
            if (intervals[i].start < intervals[i - 1].end) {
                return false;
            }
        }
        return true;
    }
};
