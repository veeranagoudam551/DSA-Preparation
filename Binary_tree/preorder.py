class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversal(self, root):

        # If tree is empty
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:

            # Take the top node
            current = stack.pop()

            # Visit Root
            result.append(current.val)

            # Push Right first
            if current.right:
                stack.append(current.right)

            # Push Left second
            if current.left:
                stack.append(current.left)

        return result


# --------------------------------
# Creating the Binary Tree
# --------------------------------

#        1
#       /
#      4
#     / \
#    7   2

root = TreeNode(1)

root.left = TreeNode(4)

root.left.left = TreeNode(7)
root.left.right = TreeNode(2)


# --------------------------------
# Preorder Traversal
# --------------------------------

solution = Solution()

answer = solution.preorderTraversal(root)

print("Preorder Traversal:", answer)