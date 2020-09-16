from insertion import Node, insertion

def find_max(root):
    max = -99999999

    if root != None:
        left = int(find_max(root.left))
        right = int(find_max(root.right))
        if left > right :
            max = left
        else:
            max = right
        rootval = int(root.val)
        if rootval > max:
            max = root.val   
    return max

if __name__ == "__main__":
    root = insertion()
    max = find_max(root)
    print(max)