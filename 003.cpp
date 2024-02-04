#include <string>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> record;
        int result = 0;
        int start = 0;
        for (int i = 0; i < s.length(); i++) {
            if (record.find(s[i]) != record.end() && record[s[i]] >= start) {
                start = record[s[i]] + 1;
            }
            result = max(result, i-start+1); // [start,i]
            record[s[i]] = i;
        }
        return result;
    }
};

int main() {
    string s = "pwwkew";
    cout << Solution().lengthOfLongestSubstring(s) << endl;
}