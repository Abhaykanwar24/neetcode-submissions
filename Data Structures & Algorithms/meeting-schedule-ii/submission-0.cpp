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

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int n = intervals.size();
        vector<int> start;
        vector<int> endd;
        for (int i = 0; i < n; i++) {
            start.push_back(intervals[i].start);
            endd.push_back(intervals[i].end);
        }
        sort(start.begin(), start.end());
        sort(endd.begin(), endd.end());

        int l = 0;
        int r = 0;
        int count = 0 ;
        int max_count = 0;
        while (l < n && r < n){
            if (start[l] < endd[r]){
                count++;
                l++;
            }
            else {
                count--;
                r++;
            }
            max_count = max(count , max_count);


        }

        return max_count;
    }
};
