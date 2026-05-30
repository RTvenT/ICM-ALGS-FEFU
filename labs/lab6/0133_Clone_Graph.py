class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned: dict['Node', 'Node'] = {}

        def dfs(n):
            if n in cloned:
                return cloned[n]
            clone = Node(n.val)
            cloned[n] = clone
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)


def main():
    solve = Solution()

    # Graph: 1 -- 2
    #        |    |
    #        4 -- 3
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    cloned = solve.cloneGraph(n1)
    print(cloned.val)                              # 1
    print([n.val for n in cloned.neighbors])       # [2, 4]
    print(cloned is n1)                            # False


if __name__ == '__main__':
    main()
