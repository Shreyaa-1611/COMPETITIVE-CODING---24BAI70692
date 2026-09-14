class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def inorderSuccessor(root, p):
    successor = None

    while root is not None:
        if p < root.val:
            successor = root
            root = root.left
        else:
            root = root.right

    return successor


# User Input
values = list(map(int, input("Enter BST values: ").split()))
p = int(input("Enter p value: "))

# Build BST
root = None

for value in values:
    root = insert(root, value)

# Find successor
answer = inorderSuccessor(root, p)

# Print answer
if answer is not None:
    print("Inorder Successor:", answer.val)
else:
    print("Inorder Successor: None")