class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

def getNodeFromCMD():
    print("Please enter data for node:")
    temp = Node(input())
    return temp

def insertion():

    temp = getNodeFromCMD()

    root = temp
    print("Is root has left Node(1/0):")
    isLeft = input()
    if isLeft == '1':
        root.left = insertion()
    print("Is root has right Node(1/0):")
    isRight = input()
    if isRight == '1':
        root.right = insertion()

    return root

def Traversal(root ):
    if root == None: 
        return    
    print(root.val +" ")
    Traversal(root.left)
    Traversal(root.right)

if __name__ == "__main__":
    
    root  = insertion()
    Traversal(root)
 
