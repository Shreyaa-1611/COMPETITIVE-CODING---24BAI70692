class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def findPath(root, target, path):
            if not root:
                return False

            path.append(root)

            if root == target:
                return True

            if findPath(root.left, target, path) or findPath(root.right, target, path):
                return True

            path.pop()
            return False

        path1 = []
        path2 = []

        findPath(root, p, path1)
        findPath(root, q, path2)

        lca = None

        for i in range(min(len(path1), len(path2))):
            if path1[i] == path2[i]:
                lca = path1[i]
            else:
                break

        return lca