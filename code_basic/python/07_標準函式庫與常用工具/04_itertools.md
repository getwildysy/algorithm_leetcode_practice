# itertools 模組

`itertools` 提供了許多用於操作迭代器 (Iterators) 的高效工具函式。它們通常返回生成器，節省記憶體。

## 1. 無限迭代器

```python
import itertools

# count(start, step): 從 start 開始無限計數
counter = itertools.count(10, 2)
print(next(counter)) # 10
print(next(counter)) # 12

# cycle(iterable): 無限循環序列
cycler = itertools.cycle('ABC')
# A -> B -> C -> A -> B ...

# repeat(elem, times): 重複元素
repeater = itertools.repeat(10, 3)
print(list(repeater)) # [10, 10, 10]
```

## 2. 排列與組合

```python
data = ['A', 'B', 'C']

# 排列 (Permutations): 有順序
# 取 2 個
print(list(itertools.permutations(data, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 組合 (Combinations): 無順序，不重複
print(list(itertools.combinations(data, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 組合 (包含重複元素)
print(list(itertools.combinations_with_replacement(data, 2)))
```

## 3. 其他常用工具

```python
# chain: 串接多個迭代器
print(list(itertools.chain([1, 2], [3, 4]))) # [1, 2, 3, 4]

# zip_longest: 類似 zip，但以最長的為準，不足補 fillvalue
names = ['Alice', 'Bob']
ages = [25, 30, 35]
print(list(itertools.zip_longest(names, ages, fillvalue=None)))
# [('Alice', 25), ('Bob', 30), (None, 35)]

# product: 笛卡兒積 (類似巢狀迴圈)
print(list(itertools.product([1, 2], ['a', 'b'])))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```
