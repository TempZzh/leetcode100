#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> map(512, 0);
        for (char c : t) {
            map[c] ++;
        }
        int counter = t.size(), start = 0, end = 0, pos = 0, n = INT_MAX;
        while (end < s.size()) {
            if (map[s[end++]]-- > 0) {
                counter --;
            }
            while (counter == 0) {
                if (end - start < n) {
                    pos = start;
                    n = end - start;
                }
                if (map[s[start++]]++ == 0) {
                    counter ++;
                }
            }
        }
        return n == INT_MAX ? "" : s.substr(pos, n);
    }
};

int main() {
    cout << Solution().minWindow("ADOBECODEBANC", "ABC") << endl;
}