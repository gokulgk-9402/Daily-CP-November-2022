static bool comp(vector<int> &x, vector<int> &y){
	return x[1] < y[1];
}
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), comp);
        int length = intervals.size();

        if (length<2)
            return 0;

        int ans = 0;
        int curr = intervals[0][1];

        for (int i=1; i<length; i++) {
            if (intervals[i][0] < curr) {
                ans++;
                curr = min(curr, intervals[i][1]);
            }
            else {
                curr = intervals[i][1];
            }
        }
        return ans;
    }
};