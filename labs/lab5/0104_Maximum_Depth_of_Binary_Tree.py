from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def main():
    solve = Solution()

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(solve.maxDepth(root))  # 3

    root2 = TreeNode(1, None, TreeNode(2))
    print(solve.maxDepth(root2))  # 2


if __name__ == '__main__':
    main()
