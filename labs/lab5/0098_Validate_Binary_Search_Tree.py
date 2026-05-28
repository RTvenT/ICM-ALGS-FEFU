from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lo, hi):
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)

        return validate(root, float('-inf'), float('inf'))


def main():
    solve = Solution()

    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(solve.isValidBST(root))  # True

    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(solve.isValidBST(root2))  # False


if __name__ == '__main__':
    main()
