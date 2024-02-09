#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<vector<int>> m (matrix);
        for (int i = 0; i < m.size(); i++) {
            for (int j = 0; j < m[0].size(); j++) {
                if (m[i][j] == 0) {
                    helper(matrix, i, j);
                }
            }
        }
    }
    void helper(vector<vector<int>>& matrix, int row, int col) {
        for (int j = 0; j < matrix[0].size(); j++) {
            matrix[row][j] = 0;
        }
        for (int i = 0; i < matrix.size(); i++) {
            matrix[i][col] = 0;
        }
    }
};

int main() {
    vector<int> a = {1,2,3};
    auto b(a);
    b[0] = 100;
    cout << a[0] << endl;
}