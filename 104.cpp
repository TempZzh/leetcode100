#include <algorithm>
#include <queue>
#include <tuple>
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
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        return max(maxDepth(root->left), maxDepth(root->right));
    }
};

class Solution2 {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        int result = 0;
        queue<tuple<TreeNode*, int>> q;
        q.push(make_tuple(root, 1));
        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            result = max(result, get<1>(cur));
            if (get<0>(cur)->left != nullptr) q.push( make_tuple(get<0>(cur)->left, get<1>(cur)+1) );
            if (get<0>(cur)->right != nullptr) q.push( make_tuple(get<0>(cur)->right, get<1>(cur)+1) );
        }
        return result;
    }
};

int main() {}