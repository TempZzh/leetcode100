#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>&& nums) {
        sort(nums.begin(), nums.end());
        if (nums[0] > 1) return 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > 1 && nums[i] - nums[i-1] > 1) return nums[i-1] < 1 ? 1 : nums[i-1] + 1;
        }
        return nums[nums.size()-1] > 0 ? nums[nums.size()-1] + 1 : 1;
    }
};
// [-60, -2, -1, 40, 43]

int main () {
    // vector v = {-1,-2,-60,40,43};
    cout << Solution().firstMissingPositive({-1,-2,-60,40,43}) << endl;
}