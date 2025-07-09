// Recursive
// T.C.->O(n)
// S.C.->O(n)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void traverse(TreeNode* node, int level, vector<vector<int>>& result) {
        if (!node) return;
        
        // If we're entering a new level, create a new vector
        if (result.size() == level)
            result.push_back(vector<int>());
        
        result[level].push_back(node->val);

        traverse(node->left, level + 1, result);
        traverse(node->right, level + 1, result);
    }

    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        traverse(root, 0, result);
        return result;
    }
};

// Iterative
// T.C.->O(n)
// S.C.->O(n)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(root== NULL)
            return ans;
        queue<TreeNode*>q;
        q.push(root);
        while(!q.empty())
        {
            int size=q.size();
            vector<int> level;
            for(int i=0;i<size;i++)
            {
                TreeNode* node=q.front();
                q.pop();
                if(node->left!=NULL)
                    q.push(node->left);
                if(node->right!=NULL)
                    q.push(node->right);
                level.push_back(node->val);
            }
            ans.push_back(level);
        }
        return ans;
    }
};
