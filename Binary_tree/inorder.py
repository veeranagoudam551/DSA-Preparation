class treeNode:   #It creates a blueprint/template for a tree node.
    def __init__(self,val=0,left=None,right=None):  #This is called a constructor #Every node in our binary tree will have: value left child a right child
        selfval=val
        self.left=left     #__init__ automatically runs when you create a new TreeNode.
        self.right=right   #self means The current node/object.

    class solution:
        def inorder_traversal(self,root):
            result=[]
            stack=[]
            current=root

            while current or stack:
                while current:
                    stack.append(current)
                    current=current.left

                current=stack.pop()
                result.append(current.val)
                current=current.right

            return result

root=treeNode(1)
root.left=treeNode(4)
root.left.left=treeNode(7)
root.left.right=treeNode(2)

solution=solution()
answer=solution.inorderTraversal(root)
print(answer)





#A class is a blueprint/template for creating objects.
#Why do we use a Class?
#Because we want to create many objects with the same structure
#For a binary tree, every node needs:
#Value
#Left child
#Right child

#Instead of writing the same structure again and again, we create one blueprint: