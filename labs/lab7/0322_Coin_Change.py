from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


def main():
    solve = Solution()

    print(solve.coinChange([1, 5, 10, 25], 36))  # 3 (25+10+1)
    print(solve.coinChange([1, 2, 5], 11))        # 3 (5+5+1)
    print(solve.coinChange([2], 3))               # -1


if __name__ == '__main__':
    main()
