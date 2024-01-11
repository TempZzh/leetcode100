#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int red = 0;
        int white = 0;
        int blue = nums.size() - 1;
        while (white <= blue) {
            if (nums[white] == 0) {
                swap(nums[red++], nums[white++]);
            } else if (nums[white] == 1) {
                white++;
            } else {
                swap(nums[blue--], nums[white]);
            }
        }
    }
};

int main() {
    vector<int> nums = {2,0,2,1,1,0};
    Solution().sortColors(nums);
    for (auto n : nums) {
        cout << n << endl;
    }
    return 0;
}
// 2 0 2 1 1 0
// 0 0 2 1 1 2
// 0 0 2 1 1 2
// 0 0 1 1 2 2