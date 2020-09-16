from insertion import insertion

# InOrder teaversal
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right) 
# PreOrder teaversal
def PreOrder(root):
    if root == None:
        return
    print(root.val)
    PreOrder(root.left)
    PreOrder(root.right) 
# PostOrder teaversal 
def PostOrder(root):
    if root == None:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.val)

if __name__ == "__main__":
    root = insertion()
    print("Inorder traversal")
    inorder(root)
    print("Preorder traversal")
    PreOrder(root)
    print("post order traversal")
    PostOrder(root)