from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0

        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)

        return prev1


def main():
    solve = Solution()

    print(solve.rob([1, 2, 3, 1]))   # 4
    print(solve.rob([2, 7, 9, 3, 1]))  # 12


if __name__ == '__main__':
    main()
