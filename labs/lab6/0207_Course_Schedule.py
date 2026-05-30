class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        state = [0] * numCourses

        def has_cycle(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            state[node] = 1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = 2
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True


def main():
    solve = Solution()

    print(solve.canFinish(2, [[1, 0]]))           # True
    print(solve.canFinish(2, [[1, 0], [0, 1]]))   # False
    print(solve.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]))  # True


if __name__ == '__main__':
    main()
