from insertion import insertion,Node


def searchKey(root,key):
    if root == None:
        return False
    if root.val == key:
        return True
    
    leftSubTree = searchKey(root.left,key)
    rightSubTree = searchKey(root.right,key)
    return False

if __name__ == __name__:
    print("Please Enter Tree")
    root = insertion()
    print("Please enter search element:")
    key = int(input())
    print("Is key present : "+str(searchKey(root, key)))