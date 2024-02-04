#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> map;
        for (auto str : strs) {
            string key = str;
            sort(key.begin(), key.end());
            map[key].push_back(str);
        }

        vector<vector<string>> result;
        result.reserve(map.size());
        for (auto item : map) {
            result.push_back(item.second);
        }
        return result;
    }
};

int main() {
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    const auto& vec = Solution().groupAnagrams(strs);
    for (auto& v : vec) {
        for (auto& s : v) cout << s << " ";
        cout << endl;
    }
    return 0;
}