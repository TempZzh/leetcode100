#include <iostream>
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// Divide-and-conquer
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        return generateSubTrees(1, n);
    }
private:
    vector<TreeNode*> generateSubTrees(int start, int end) {
        vector<TreeNode*> result;
        if (start > end) {
            result.push_back(nullptr);
            return result;
        }
        for (int i = start; i <= end; i++) {
            auto leftSubTrees = generateSubTrees(start, i-1);
            auto rightSubTrees = generateSubTrees(i+1, end);
            for (auto left : leftSubTrees) {
                for (auto right : rightSubTrees) {
                    auto root = new TreeNode(i);
                    root->left = left;
                    root->right = right;
                    result.push_back(root);
                }
            }
        }
        return result;
    }
};

// DP
class Solution2 {
public:
    vector<TreeNode*> generateTrees(int n) {
        vector<TreeNode*> result[n+1];
        result[0] = {nullptr}; // 1 <= n <= 8
        for (int i = 1; i <= n; i++) {
            result[i] = {};
            for (int j = 0; j < i; j++) {
                for (auto left : result[j]) {
                    for (auto right : result[i-j-1]) {
                        auto root = new TreeNode(j+1);
                        root->left = left;
                        root->right = clone(right, j+1);
                        result[i].push_back(root);
                    }
                }
            }
        }
        return result[n];
    }
private:
    TreeNode* clone(TreeNode* n, int offset) {
        if (n == nullptr) {
            return nullptr;
        }
        auto node = new TreeNode(n->val + offset);
        node->left = clone(n->left, offset);
        node->right = clone(n->right, offset);
        return node;
    }
};

int main() {
    return 0;
}
