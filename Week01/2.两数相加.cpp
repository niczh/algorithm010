/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode root(0);
        ListNode *p = &root;
        int flag = 0;
        while(l1 || l2 || flag){
            int sum = 0;
            if(l1 != NULL) sum += l1->val;
            if(l2 != NULL) sum += l2->val;
            sum += flag;

            flag = sum / 10;
            sum %= 10;
            
            ListNode *next = new ListNode(sum);
            next->val = sum;
            p->next = next;
            p = p->next;
            l1 = l1 ? l1->next : NULL;
            l2 = l2 ? l2->next : NULL;
        }
        return root.next;
    }
};
// @lc code=end

