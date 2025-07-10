#T.C.->O(n)
#S.C.->O(n)
# Recursive
class Solution:
    def postorder(self, root, ans):
        if(root is None):
            return
        self.postorder(root.left, ans)
        self.postorder(root.right, ans)
        ans.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.postorder(root, ans)
        return ans

# 2-Stack Iterative
# T.C.->O(n)
# S.C.->O(2n)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        st1 = [root]
        st2 = []
        postorder = []
        while st1:
            node = st1.pop()
            st2.append(node)
            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)

        while st2:
            postorder.append(st2.pop().val)

        return postorder


# 1-Stack Iterative
# T.C.->O(2n)
# S.C.->O(n)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        if not root:
            return postorder
        stack = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1].right
                if not temp:
                    temp = stack.pop()
                    postorder.append(temp.val)
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        postorder.append(temp.val)
                else:
                    curr = temp

        return postorder
