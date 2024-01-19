#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (left == right) {
            return head;
        }
        auto dummy = new ListNode();
        dummy->next = head;
        auto p = dummy;
        for (int i = 0; i < left-1; i++) {
            p = p->next;
        }
        auto tail = p->next;
        for (int i = 0; i < right-left; i++) {
            auto tmp = p->next;
            p->next = tail->next;
            tail->next = tail->next->next;
            p->next->next = tmp;
        }
        return dummy->next;
    }
};

int main() {
    std::cout << "result:" << std::endl;
    return 0;
}
