# Recursive
# T.C.->O(n)
# S.C.->O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, ans):
        if(root is None):
            return
        ans.append(root.val)
        self.preorder(root.left, ans)
        self.preorder(root.right, ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.preorder(root, ans)
        return ans        


# Iterative
# T.C.->O(n)
# S.C.->O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        preorder = []

        while stack:
            node = stack.pop()
            preorder.append(node.val)
            # Push right first so left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return preorder 
