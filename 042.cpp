#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int res = 0;
        int i = 0;
        int j = height.size() - 1;
        int i_max = 0;
        int j_max = height.size() - 1;
        while (i < j) {
            if (height[i_max] < height[j_max]) {
                i++;
                if (height[i_max] > height[i]) {
                    res += (height[i_max] - height[i]);
                } else {
                    i_max = i;
                }
            } else { // height[i_max] >= height[j_max]
                j--;
                if (height[j_max] > height[j]) {
                    res += (height[j_max]- height[j]);
                } else {
                    j_max = j;
                }
            }
        }
        return res;
    }
};

int main()
{
    vector<int> vec = {4, 2, 0, 3, 2, 5};
    cout << Solution().trap(vec) << endl;
    return 0;
}
