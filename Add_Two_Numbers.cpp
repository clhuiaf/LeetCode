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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        // Define a new list
        ListNode* head = nullptr;

        // Define working pointers
        ListNode* p_head;
        ListNode* p_leading;
        ListNode* p_secondary;

        // Define counters
        int val = 0;
        int carry = 0;
        int l1_length = 0;
        int l2_length = 0;

        // Create the first node
        val = (l1->val + l2->val) % 10;
        head = new ListNode(val);
        carry = ((l1->val + l2->val) >= 10) ? 1 : 0;
        p_head = head;

        // Length checking
        for (ListNode* p = l1; p != nullptr; p = p->next) {
            l1_length++;
        }
        for (ListNode* p = l2; p != nullptr; p = p->next) {
            l2_length++;
        }

        // Return if both list has length 1 only (We are done)
        if (l1_length == 1 && l2_length == 1) {

            // If sum of first node of both list >= 10;
            if (carry != 0) {
                p_head->next = new ListNode(carry);
            }

            return head;
        }

        // Determine leading and secondary pointers
        if (l1_length > l2_length) {
            p_leading = l1->next;
            p_secondary = l2->next;
        } else if (l1_length < l2_length) {
            p_leading = l2->next;
            p_secondary = l1->next;
        } else {
            p_leading = l1->next;
            p_secondary = l2->next;
        }

        // Add two numbers up to same length
        // Short-Circuit when the secondary list terminated
        // If both has the same length , terminated together
        while (p_secondary != nullptr && p_leading != nullptr) {

            // Calculate values and carry
            // Create next node
            val = (p_leading->val + p_secondary->val + carry) % 10;
            p_head->next = new ListNode(val);
            carry = ((p_leading->val + p_secondary->val + carry) >= 10) ? 1 : 0;

            // Move pointers to next positions
            p_head = p_head->next;
            p_leading = p_leading->next;
            p_secondary = p_secondary->next;
        }

        if (l1_length == l2_length) {

            if (carry != 0) {
                p_head->next = new ListNode(carry);
                p_head = p_head->next;
                carry = 0;
            }

        } else {

            while (p_leading != nullptr) {
                val = (p_leading->val + carry) % 10;
                p_head->next = new ListNode(val);
                carry = (p_leading->val + carry) >= 10 ? 1 : 0;
                p_head = p_head->next;
                p_leading = p_leading->next;
            }

            if (carry != 0) {
                p_head->next = new ListNode(carry);
                p_head = p_head->next;
                carry = 0;
            }
        }

        return head;
    }
};