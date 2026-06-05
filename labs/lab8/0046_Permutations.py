from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int) -> None:
            if start == len(nums):
                result.append(list(nums))
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result


def main():
    solve = Solution()

    print(solve.permute([1, 2, 3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(solve.permute([0, 1]))     # [[0,1],[1,0]]
    print(solve.permute([1]))        # [[1]]


if __name__ == '__main__':
    main()
