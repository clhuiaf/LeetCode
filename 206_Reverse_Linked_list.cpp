struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        // Define a new head;
        ListNode* new_head = nullptr;

        // Define working pointers
        ListNode* p = nullptr;
        ListNode* prev = nullptr;
        ListNode* current = head;

        // Define boolean
        bool hasNode = 0;

        // No node -> return no node
        if (head == nullptr) {
            return nullptr;
        }
        // Only one node -> return that no without reverse
        else if (head->next == nullptr) {
            new_head = new ListNode(head->val);
            return new_head;
        }

        // At least more than one nodes -> reverse the linked list
        while (prev != head) {

            // Stop before the prev one
            while (current->next != prev) {
                current = current->next;
            }

            if (!hasNode) {
                new_head = new ListNode(current->val);
                p = new_head;
                prev = current;
                hasNode = 1;
                current = head;
            }

            else {
                p->next = new ListNode(current->val);
                p = p->next;
                prev = current;
                current = head;
            }
        }

        return new_head;
    }
};