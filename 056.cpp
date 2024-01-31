#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> result;
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b){
            return a[0] < b[0];
        });
        auto newInterval = intervals[0];
        for (auto interval : intervals) {
            if (newInterval[1] >= interval[0]) {
                newInterval[1] = max(newInterval[1], interval[1]);
            } else {
                result.push_back(newInterval);
                newInterval = interval;
            }
        }
        result.push_back(newInterval);
        return result;
    }
};

int main() {
    vector<vector<int>> intervals{{1,3}, {2,6}, {8,10}, {15,18}};
    auto result = Solution().merge(intervals);
    for (auto e : result) {
        cout << "[" << e[0] << ", " << e[1] << "]" << endl;
    }
    return 0;
}