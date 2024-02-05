#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];
        int tmpSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (tmpSum + nums[i] < 0) {
                tmpSum = 0;
                maxSum = max(maxSum, nums[i]);
            } else {
                tmpSum += nums[i];
                maxSum = max(maxSum, tmpSum);
            }
        }
        return maxSum;
    }
};

int main() {
    vector<int> nums{-2,1,-3,4,-1,2,1,-5,4};
    cout << Solution().maxSubArray(nums) << endl;
}