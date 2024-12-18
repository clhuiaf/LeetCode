
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Working pointers for both lists
        ListNode* p1 = list1;
        ListNode* p2 = list2; 
        bool l1_is_greater = true;

        // Deal with edge cases
        if (p1 == nullptr && p2 == nullptr)
            return nullptr;
        if (p1 == nullptr || p2 == nullptr){
            return p1 ? p1 : p2;
        }

        //Initialize working pointers
        if (list1->val >= list2->val){
            p1 = list1;
            p2 = list2;
        }
        else{
            p1 = list2;
            p2 = list1;
            l1_is_greater = false;
        }

        while (p1 != nullptr){
            if (p2->next != nullptr){
                if (p1->val >= p2->val && p1->val <= p2->next->val){
                    p2->next = new ListNode(p1->val, p2->next);
                    p1 = p1->next;
                    p2 = p2->next;
                }
                else if (p1->val >= p2->val && p1->val >= p2->next->val){
                    p2 = p2->next;
                }
            }
            else{
                if (p1->val >= p2->val){
                    p2->next = new ListNode(p1->val);
                    p1 = p1->next;
                    p2 = p2->next;
                }
            }
        }
        return l1_is_greater ? list2 : list1;
    }
};