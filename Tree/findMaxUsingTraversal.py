from insertion import Node, insertion

def findMaxUsingTraversal(root, max):
    if root == None:
        return max 
    
    max = findMaxUsingTraversal(root.left,max)
    max = findMaxUsingTraversal(root.right,max)

    if int(root.val) > max:
        max = int(root.val)

    return max

if __name__ == __name__:
    root = insertion()
    val = int(root.val)
    max = findMaxUsingTraversal(root,val)
    print(max)