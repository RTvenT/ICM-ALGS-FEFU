# Лабораторная работа №8 — Перебор с возвратом (Backtracking)

## Теория

### Перебор с возвратом (Backtracking)

**Backtracking** — метод полного перебора с отсечением: строим решение пошагово, и если на каком-то шаге текущий путь заведомо не может привести к ответу — откатываемся (возврат) и пробуем другой вариант.

Три составные части любого backtracking-решения:
- **Выбор** — что добавляем на текущем шаге
- **Ограничение** — когда путь заведомо тупиковый и нужно обрезать дерево перебора
- **Цель** — когда частичное решение является полным

Шаблон:

```python
def backtrack(state):
    if is_goal(state):
        result.append(copy(state))
        return
    for choice in get_choices(state):
        state.apply(choice)
        backtrack(state)
        state.undo(choice)      # откат
```

**Ключевой момент:** после рекурсивного вызова обязательно отменяем сделанный выбор (`pop`, swap обратно, снять пометку). Это и есть «возврат».

---

## Задачи

---

### #78 — Subsets

**Условие:** дан массив уникальных чисел `nums`. Вернуть все возможные подмножества (включая пустое).

**Идея:** на каждом шаге мы добавляем текущий элемент в подмножество и рекурсивно продолжаем со следующего индекса. Параметр `start` гарантирует, что мы не берём элементы повторно и не генерируем дубли.

```
nums = [1, 2, 3]

backtrack(0, []):
  добавляем []
  i=0: backtrack(1, [1])
    добавляем [1]
    i=1: backtrack(2, [1,2])
      добавляем [1,2]
      i=2: backtrack(3, [1,2,3]) → добавляем [1,2,3]
    i=2: backtrack(3, [1,3]) → добавляем [1,3]
  i=1: backtrack(2, [2])
    добавляем [2]
    i=2: backtrack(3, [2,3]) → добавляем [2,3]
  i=2: backtrack(3, [3]) → добавляем [3]
```

**Сложность:** O(n × 2ⁿ) по времени (2ⁿ подмножеств, каждое копируем за O(n)), O(n) по стеку рекурсии.

```python
def subsets(self, nums):
    result = []
    def backtrack(start, current):
        result.append(list(current))
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result
```

---

### #46 — Permutations

**Условие:** дан массив различных чисел `nums`. Вернуть все возможные перестановки.

**Идея (swap):** фиксируем позицию `start` и перебираем, какой из оставшихся элементов поставить туда — меняем местами `nums[start]` и `nums[i]`, рекурсируем для `start+1`, затем меняем обратно.

```
nums = [1, 2, 3], start=0

swap(0,0): [1,2,3] → backtrack(1)
  swap(1,1): [1,2,3] → backtrack(2)
    swap(2,2): [1,2,3] → добавляем [1,2,3]
  swap(1,2): [1,3,2] → backtrack(2)
    swap(2,2): [1,3,2] → добавляем [1,3,2]
  swap(1,2): откат → [1,2,3]
swap(0,1): [2,1,3] → ...
swap(0,2): [3,2,1] → ...
```

**Ключевой момент:** swap в обратном порядке после рекурсии восстанавливает массив. Нет нужды в отдельном списке «использованных» элементов.

**Сложность:** O(n × n!) по времени, O(n) по стеку рекурсии.

```python
def permute(self, nums):
    result = []
    def backtrack(start):
        if start == len(nums):
            result.append(list(nums))
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    backtrack(0)
    return result
```

---

### #39 — Combination Sum

**Условие:** дан массив различных чисел `candidates` и число `target`. Найти все комбинации, дающие сумму `target`. Один элемент можно использовать несколько раз.

**Идея:** при рекурсии передаём тот же индекс `i` (не `i+1`), позволяя повторно выбирать элемент. Параметр `remaining` отслеживает оставшуюся сумму — если он стал 0, нашли комбинацию; если кандидат больше остатка — пропускаем (отсечение).

```
candidates = [2, 3, 6, 7], target = 7

backtrack(0, [], 7):
  i=0 (2): backtrack(0, [2], 5)
    i=0 (2): backtrack(0, [2,2], 3)
      i=0 (2): backtrack(0, [2,2,2], 1)
        i=0 (2): 2 > 1 — стоп
        i=1 (3): 3 > 1 — стоп
      i=1 (3): backtrack(1, [2,2,3], 0) → добавляем [2,2,3]
    i=1 (3): backtrack(1, [2,3], 2)
      i=1 (3): 3 > 2 — стоп
    ...
  i=3 (7): backtrack(3, [7], 0) → добавляем [7]
```

**Сложность:** O(n^(T/min)) в худшем случае, где T — target, min — минимальный кандидат.

```python
def combinationSum(self, candidates, target):
    result = []
    def backtrack(start, current, remaining):
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
```

---

### #79 — Word Search

**Условие:** дана сетка символов `board` и строка `word`. Определить, можно ли найти слово в сетке, двигаясь по соседним (горизонтально/вертикально) клеткам. Одну клетку нельзя использовать дважды.

**Идея:** для каждой клетки запускаем DFS. На каждом шаге проверяем, что текущая клетка совпадает с нужным символом слова, временно помечаем её посещённой (`'#'`), рекурсируем в 4 стороны, затем восстанавливаем символ обратно.

```
board:        word = "ABCCED"
A B C E
S F C S
A D E E

Старт (0,0)='A' → (0,1)='B' → (0,2)='C' → (0,3)='E'?
  нет, E≠C — откат
→ (1,2)='C' → (2,2)='E' → (2,1)='D' → True ✓
```

**Отсечения:**
- Выход за границы сетки
- Символ не совпадает с нужным символом слова
- Клетка помечена как посещённая (`board[r][c] == '#'`)

**Сложность:** O(m × n × 4^L) в худшем случае, где L — длина слова. На практике намного быстрее из-за ранних отсечений.

```python
def exist(self, board, word):
    rows, cols = len(board), len(board[0])
    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
        temp = board[r][c]
        board[r][c] = '#'
        found = (dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1))
        board[r][c] = temp
        return found
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```

---

## Сводная таблица

| # | Задача | Подход | Время | Память |
|---|---|---|---|---|
| 78 | Subsets | Backtracking (выбор/пропуск) | O(n × 2ⁿ) | O(n) |
| 46 | Permutations | Backtracking (swap) | O(n × n!) | O(n) |
| 39 | Combination Sum | Backtracking (с повтором) | O(n^(T/min)) | O(T/min) |
| 79 | Word Search | DFS + временная пометка | O(m×n × 4^L) | O(L) |

> n — размер входного массива, T — target, min — минимальный кандидат, L — длина слова, m×n — размер сетки.
