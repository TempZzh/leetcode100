#include <iostream>
#include <vector>
#include <stack>
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

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> stack;
        auto cur = root;
        while (cur != nullptr || !stack.empty()) {
            while (cur != nullptr) {
                stack.push(cur);
                cur = cur->left;
            }
            cur = stack.top();
            stack.pop();
            ans.push_back(cur->val);
            cur = cur->right;
        }
        return ans;
    }
};

int main() {
    auto root = TreeNode();
    for (auto e : Solution().inorderTraversal(&root)) {
        cout << e << endl;
    }
    return 0;
}
