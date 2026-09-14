class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    if root is None or root.val == p or root.val == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# User Input
values = list(map(int, input("Enter tree elements (use -1 for NULL): ").split()))
p = int(input("Enter p: "))
q = int(input("Enter q: "))

# Create tree
nodes = [None if x == -1 else TreeNode(x) for x in values]

for i in range(len(nodes)):
    if nodes[i] is not None:
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            nodes[i].left = nodes[left]

        if right < len(nodes):
            nodes[i].right = nodes[right]

root = nodes[0]

result = lowestCommonAncestor(root, p, q)

print("Output:", result.val)