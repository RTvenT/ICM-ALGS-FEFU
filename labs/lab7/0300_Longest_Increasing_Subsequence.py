from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)


def main():
    solve = Solution()

    print(solve.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4 (2,3,7,101)
    print(solve.lengthOfLIS([0, 1, 0, 3, 2, 3]))             # 4 (0,1,2,3)
    print(solve.lengthOfLIS([7, 7, 7, 7, 7]))                # 1


if __name__ == '__main__':
    main()
