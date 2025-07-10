//T.C.->O(n)
//S.C.->O(n)
// Recursive
class Solution {
public:
    void postorder(TreeNode* root, vector<int> &ans)
    {
        if(root==NULL)
            return;
        postorder(root->left, ans);
        postorder(root->right, ans);
        ans.push_back(root->val);
    }
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        postorder(root, ans);
        return ans;
    }
};

//2-Stack Iterative
// T.C.->O(n)
// S.C.->O(2n)
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> postorder;
        if(root == NULL) return postorder;
        stack<TreeNode*> st1, st2;
        st1.push(root);
        while(!st1.empty()) {
            root =st1.top();
            st1.pop();
            st2.push(root);
            if(root->left!=NULL)
                st1.push(root->left);
            if(root->right!=NULL)
                st1.push(root->right);
        }
        while(!st2.empty()) {
            postorder.push_back(st2.top()->val);
            st2.pop();
        }
        return postorder;
    }
};

//1-Stack Iterative
// T.C.->O(2n)
// S.C.->O(n)
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> postorder;
        if(root == NULL) 
            return postorder;
        stack<TreeNode*> st;
        TreeNode* curr = root;
        while (!st.empty() || curr != NULL){
            if (curr != NULL) {
                st.push(curr);
                curr = curr->left;
            }
            else {
                TreeNode* temp = st.top()->right;
                if (temp == NULL) {
                    temp = st.top();
                    st.pop();
                    postorder.push_back(temp->val);
                    while (!st.empty() && temp == st.top()->right) {
                        temp = st.top();
                        st.pop();
                        postorder.push_back(temp->val);
                    }
                }
                else
                    curr = temp;
            }
        }
    return postorder;
    }
};
