from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, current: List[int], remaining: int) -> None:
            if remaining == 0:
                result.append(list(current))
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= remaining:
                    current.append(candidates[i])
                    backtrack(i, current, remaining - candidates[i])
                    current.pop()

        backtrack(0, [], target)
        return result


def main():
    solve = Solution()

    print(solve.combinationSum([2, 3, 6, 7], 7))   # [[2,2,3],[7]]
    print(solve.combinationSum([2, 3, 5], 8))       # [[2,2,2,2],[2,3,3],[3,5]]
    print(solve.combinationSum([2], 1))             # []


if __name__ == '__main__':
    main()
