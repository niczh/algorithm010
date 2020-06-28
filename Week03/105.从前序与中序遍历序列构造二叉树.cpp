/*
 * @lc app=leetcode.cn id=105 lang=cpp
 *
 * [105] 从前序与中序遍历序列构造二叉树
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
    unordered_map<int, int> inIdxMap;
    TreeNode* helper(vector<int>& preorder, vector<int>& inorder, int preIdx, int start, int end) {
        if (start ==  end) return NULL;

        int val = preorder[preIdx];
        int inIdx = inIdxMap[val];

        TreeNode* root = new TreeNode(val);

        root->left = helper(preorder, inorder, preIdx + 1, start, inIdx);
        root->right = helper(preorder, inorder, preIdx + 1 + inIdx - start, inIdx + 1, end);

        return root;
    };
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() != inorder.size() || preorder.size() == 0) 
            return NULL;
        
        for (int i = 0; i < preorder.size(); ++i) {
            inIdxMap[inorder[i]] = i;
        }

        return helper(preorder, inorder, 0, 0, preorder.size());
    }
};
// @lc code=end

