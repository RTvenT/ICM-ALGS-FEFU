from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(1, rows)]
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows - 1)]

        pac = bfs(pacific_starts)
        atl = bfs(atlantic_starts)

        return [[r, c] for r in range(rows) for c in range(cols) if (r, c) in pac and (r, c) in atl]


def main():
    solve = Solution()

    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    print(solve.pacificAtlantic(heights))
    # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]


if __name__ == '__main__':
    main()
