# Лабораторная работа №6 — Графы

## Теория

### Граф

**Граф** — структура данных из **вершин (nodes/vertices)** и **рёбер (edges)**, соединяющих пары вершин.

```
1 — 2
|   |
4 — 3
```

Основные виды:
- **Ориентированный (directed)** — рёбра имеют направление: `A → B` не означает `B → A`
- **Неориентированный (undirected)** — ребро двустороннее
- **Взвешенный** — каждое ребро имеет вес
- **Циклический / ацикличный (DAG)** — наличие или отсутствие циклов

---

### Представление графа

| Способ | Структура | Когда использовать |
|---|---|---|
| Список смежности | `dict / list[list]` | разреженный граф (мало рёбер) |
| Матрица смежности | `list[list[bool]]` | плотный граф, быстрая проверка ребра |
| Множество рёбер | `list[tuple]` | построение графа из входных данных |

В задачах LeetCode чаще всего строят **список смежности**:

```python
graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u].append(v)
```

---

### DFS на графе

**DFS (Depth-First Search)** — обход вглубь. Используем рекурсию или явный стек. Обязательно отслеживаем посещённые вершины, чтобы не зациклиться.

```python
visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor)
```

**Три состояния вершины** (для поиска цикла):
- `0` — не посещена
- `1` — в стеке текущего пути DFS (visiting)
- `2` — полностью обработана (done)

Если DFS встречает вершину в состоянии `1` — найден цикл.

---

### BFS на графе

**BFS (Breadth-First Search)** — обход вширь с очередью. Даёт кратчайший путь в невзвешенном графе.

```python
from collections import deque

visited = set([start])
queue = deque([start])

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

---

### DFS на сетке (grid)

Двумерная сетка — частный случай графа, где каждая клетка `(r, c)` связана с 4 соседями. Вместо `visited` часто модифицируют саму сетку (например, `'1' → '0'`).

```
  (r-1, c)
     ↑
(r, c-1) ← (r, c) → (r, c+1)
     ↓
  (r+1, c)
```

---

### Связные компоненты

**Связная компонента** — максимальное подмножество вершин, в котором каждая пара вершин достижима друг из друга. Подсчёт компонент: запустить DFS/BFS для каждой непосещённой вершины, считая запуски.

---

### Топологическая сортировка и циклы

В **ориентированном графе** цикл означает, что задачи взаимозависимы и не могут быть выполнены. Проверка: DFS с тремя состояниями вершин (0/1/2). Если находим вершину в состоянии `1` при текущем DFS — цикл есть.

---

## Задачи

---

### #200 — Number of Islands

**Задача:** посчитать количество островов в двоичной сетке `'1'` (суша) / `'0'` (вода). Остров — связная группа клеток `'1'` по 4 направлениям.

**Идея:** итерируем по всей сетке. Когда находим `'1'`, запускаем DFS, который «затапливает» весь остров (заменяет `'1'` на `'0'`), и увеличиваем счётчик.

```
1 1 0 0 0       0 0 0 0 0
1 1 0 0 0  →    0 0 0 0 0   count = 1 (первый DFS потопил весь остров)
0 0 1 0 0       0 0 0 0 0   count = 2
0 0 0 1 1       0 0 0 0 0   count = 3
```

**Сложность:** O(m·n) по времени и памяти (стек рекурсии в худшем случае).

**Ключевой момент:** мутация входной сетки (`'1' → '0'`) избавляет от отдельного `visited`-множества. Если входные данные нельзя изменять — создать `visited = set()`.

```python
def numIslands(self, grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r + 1, c); dfs(r - 1, c)
        dfs(r, c + 1); dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1  
                dfs(r, c)
    return count
```

---

### #133 — Clone Graph

**Задача:** сделать полную копию (deep copy) неориентированного связного графа.

**Идея:** DFS + хэш-таблица `cloned: {исходный_узел → клон}`. При первом посещении узла создаём его клон и сразу записываем в таблицу. Затем рекурсивно клонируем всех соседей и добавляем их клоны в список соседей нового узла.

Запись в таблицу **до** рекурсии критична — это обрывает циклы: если DFS снова придёт к уже клонированному узлу, он просто вернёт готовый клон.

```
Оригинал:        Клон:
  1 — 2            1' — 2'
  |   |    →       |    |
  4 — 3            4' — 3'

cloned = {1: 1', 2: 2', 3: 3', 4: 4'}
```

**Сложность:** O(V + E) по времени и памяти.

```python
def cloneGraph(self, node):
    if not node:
        return None
    cloned = {}

    def dfs(n):
        if n in cloned:
            return cloned[n]
        clone = Node(n.val)
        cloned[n] = clone
        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone

    return dfs(node)
```

---

### #207 — Course Schedule

**Задача:** есть `n` курсов и список предпосылок `[a, b]` (чтобы взять `a`, нужно сначала взять `b`). Можно ли пройти все курсы? Эквивалентно: есть ли цикл в ориентированном графе зависимостей?

**Идея:** DFS с тремя состояниями каждой вершины:
- `0` — не посещена
- `1` — сейчас в стеке DFS (processing)
- `2` — полностью обработана (safe)

Если во время DFS мы попадаем в вершину со состоянием `1` — нашли цикл → курсы не завершить.

```
Граф: 0 → 1 → 2 → 3 → 4   (нет цикла → True)
Граф: 0 → 1 → 0            (цикл → False)

DFS от 0:
  state[0] = 1  (visiting)
  → state[1] = 1
    → state[0] == 1 → ЦИКЛ
```

**Сложность:** O(V + E) по времени, O(V) по памяти.

**Ключевой момент:** после полной обработки вершины ставим `state = 2` — это позволяет не перепроходить безопасные вершины при повторном запуске DFS с другого узла.

```python
def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = [0] * numCourses

    def has_cycle(node):
        if state[node] == 1: return True
        if state[node] == 2: return False
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
```

---

### #417 — Pacific Atlantic Water Flow

**Задача:** сетка высот. Вода течёт в соседнюю клетку, если там высота ≤ текущей. Тихий океан омывает верхний и левый края, Атлантический — нижний и правый. Найти клетки, из которых вода может достичь **обоих** океанов.

**Идея:** вместо того чтобы идти от каждой клетки к океанам (дорого), делаем **реверс**: запускаем BFS **от берегов вглубь**, двигаясь только в клетки с высотой ≥ текущей (вода «течёт назад», в гору). Получаем два множества достижимых клеток. Ответ — их пересечение.

```
Высоты:          Pacific BFS:     Atlantic BFS:    Пересечение:
1 2 2 3 5        P P P P P        . . . . A        . . . . X
3 2 3 4 4   →    P P P P P   ∩    . . . A A   =    . . . X X
2 4 5 3 1        P P P P .        . . P A A        . . X . .
6 7 1 4 5        P P . P P        A A . A A        X X . . .
5 1 1 2 4        P . . . P        A A A A A        X . . . .
```

**Сложность:** O(m·n) по времени и памяти.

**Ключевой момент:** «обратный» BFS (из океана вглубь, по возрастанию высоты) — стандартный приём для задач типа «найти источники, из которых достижима цель».

```python
def pacificAtlantic(self, heights):
    rows, cols = len(heights), len(heights[0])

    def bfs(starts):
        visited = set(starts)
        queue = deque(starts)
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return visited

    pac = bfs([(0, c) for c in range(cols)] + [(r, 0) for r in range(1, rows)])
    atl = bfs([(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows-1)])

    return [[r, c] for r in range(rows) for c in range(cols)
            if (r, c) in pac and (r, c) in atl]
```

---

## Сводная таблица

| # | Задача | Структура | Подход | Время | Память |
|---|---|---|---|---|---|
| 200 | Number of Islands | сетка | DFS + затопление | O(m·n) | O(m·n) |
| 133 | Clone Graph | граф | DFS + хэш-таблица | O(V+E) | O(V) |
| 207 | Course Schedule | орграф | DFS + 3 состояния | O(V+E) | O(V) |
| 417 | Pacific Atlantic | сетка | обратный BFS × 2 | O(m·n) | O(m·n) |

> V — число вершин, E — число рёбер, m·n — размер сетки.
