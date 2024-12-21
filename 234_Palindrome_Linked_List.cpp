//  * Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {

        ListNode* wp = head;
        ListNode* forward = head;
        ListNode* backward = nullptr;

        if (wp == nullptr || wp->next == nullptr)
            return true;

        while (forward != backward){

            if (wp->next == backward){
                if (wp->val == forward->val){
                    backward = wp;
                    if (forward != backward)
                        forward = forward->next;
                    wp = forward;
                }
                else{
                    return false;
                }
            }
            else
                wp = wp->next;

        }

        return true;

    }


};