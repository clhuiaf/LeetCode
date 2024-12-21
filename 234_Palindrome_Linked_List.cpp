//  * Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

#include <stack>

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        
        std::stack<int> stack;
        ListNode* fast = head;
        ListNode* slow = head;

        while (fast && fast->next){
            stack.push(slow->val);
            slow = slow->next;
            fast = fast->next->next;
        }

        if (fast)
            slow = slow->next;

        while (!stack.empty() && slow){
            if (stack.top() != slow->val)
                return false;
            stack.pop();
            slow = slow->next;
        }
        return true;

    }


};