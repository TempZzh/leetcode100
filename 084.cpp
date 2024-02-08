#include <vector>
#include <stack>
#include <iostream>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> s;
        int maxArea = 0;
        int tp;
        int areaOfTop;
        int i = 0;
        while (i < heights.size()) {
            if (s.empty() || heights[s.top()] <= heights[i]) {
                s.push(i++);
            } else {
                tp = s.top();
                s.pop();
                areaOfTop = heights[tp] * (s.empty() ? i : i - s.top() - 1);
                maxArea = max(maxArea, areaOfTop);
            }
        }
        while ( !s.empty() ) {
            tp = s.top();
            s.pop();
            areaOfTop = heights[tp] * (s.empty() ? i : i - s.top() - 1);
            maxArea = max(maxArea, areaOfTop);
        }
        return maxArea;
    }
};

int main() {
    vector v = { 2,1,5,6,2,3 };
    cout << Solution().largestRectangleArea(v) << endl;
}