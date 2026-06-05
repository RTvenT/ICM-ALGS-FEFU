from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int, current: List[int]) -> None:
            result.append(list(current))
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result


def main():
    solve = Solution()

    print(solve.subsets([1, 2, 3]))  # [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
    print(solve.subsets([0]))        # [[], [0]]


if __name__ == '__main__':
    main()
