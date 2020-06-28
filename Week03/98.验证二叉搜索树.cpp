/*
 * @lc app=leetcode.cn id=98 lang=cpp
 *
 * [98] 验证二叉搜索树
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
    long pre_min = LONG_MIN;
    bool isValidBST(TreeNode* root) {
        // 中序遍历
        if (root == nullptr) return true;
        if (false == isValidBST(root->left)){
            return false;
        }

        if (pre_min >= root->val) return false;

        pre_min = root->val;

        return isValidBST(root->right);    
    }
};
// @lc code=end

