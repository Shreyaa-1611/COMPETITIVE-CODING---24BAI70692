class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# Insert a value into BST
def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


# Inorder traversal
def inorder(root, arr):
    if root is None:
        return

    inorder(root.left, arr)
    arr.append(root.val)
    inorder(root.right, arr)


# Brute Force
def inorderSuccessor(root, p):
    arr = []

    inorder(root, arr)

    for i in range(len(arr)):
        if arr[i] == p:
            if i + 1 < len(arr):
                return arr[i + 1]
            return None

    return None


# -------- USER INPUT --------

values = list(map(int, input("Enter BST values: ").split()))
p = int(input("Enter p value: "))

root = None

for value in values:
    root = insert(root, value)

answer = inorderSuccessor(root, p)

if answer is not None:
    print("Inorder Successor:", answer)
else:
    print("Inorder Successor: None")