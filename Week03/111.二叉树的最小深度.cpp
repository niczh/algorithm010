/*
 * @lc app=leetcode.cn id=111 lang=cpp
 *
 * [111] 二叉树的最小深度
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (nullptr == root) return 0;
        int m1 = minDepth(root->left);
        int m2 = minDepth(root->right);
        if (nullptr != root->left && nullptr != root->right) return 1 + min(m1, m2);
        else return 1 + m1 + m2;
    }
};
// @lc code=end

