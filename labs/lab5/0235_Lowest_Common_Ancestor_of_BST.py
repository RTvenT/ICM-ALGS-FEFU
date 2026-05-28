class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


def main():
    solve = Solution()

    root = TreeNode(6,
        TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9))
    )

    p, q = root.left, root.right          # 2, 8
    print(solve.lowestCommonAncestor(root, p, q).val)   # 6

    p2, q2 = root.left, root.left.right   # 2, 4
    print(solve.lowestCommonAncestor(root, p2, q2).val) # 2


if __name__ == '__main__':
    main()
