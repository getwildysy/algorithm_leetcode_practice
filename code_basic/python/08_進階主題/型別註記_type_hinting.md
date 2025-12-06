# 型別註記 (Type Hinting)

Python 3.5+ 引入了型別註記，雖然 Python 仍然是動態型別語言（不會在執行時強制檢查型別），但加上註記可以提高程式碼可讀性，並允許 IDE 或靜態檢查工具 (如 `mypy`) 提早發現錯誤。

## 1. 基本語法

`variable: type = value`
`def func(arg: type) -> return_type:`

```python
# 變數註記
age: int = 25
name: str = "Alice"
height: float = 1.75
is_student: bool = True

# 函式註記
def greeting(name: str) -> str:
    return f"Hello, {name}"
```

## 2. 複雜型別 (`typing` 模組)

在 Python 3.9 之前，需要從 `typing` 匯入 `List`, `Dict`, `Tuple` 等。Python 3.9+ 可以直接使用內建型別 `list`, `dict`。

```python
from typing import List, Dict, Tuple, Optional, Union

# 列表：包含整數的列表
numbers: List[int] = [1, 2, 3]
# Python 3.9+: numbers: list[int] = [1, 2, 3]

# 字典：Key 為字串，Value 為整數
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# 元組：固定結構 (字串, 整數)
person: Tuple[str, int] = ("Alice", 30)

# Optional: 可以是 int 或 None
user_id: Optional[int] = None

# Union: 可以是 int 或 float
result: Union[int, float] = 10.5
```

## 3. 自訂型別與 Any

```python
from typing import Any

# Any: 接受任何型別 (等同於沒寫註記)
def print_anything(obj: Any) -> None:
    print(obj)

# 自訂類別
class User:
    pass

def get_user_name(user: User) -> str:
    return "Name"
```

## 4. 靜態檢查

安裝 `mypy`: `pip install mypy`
執行檢查: `mypy script.py`

```python
# example.py
def add(a: int, b: int) -> int:
    return a + b

add(1, "2") # mypy 會報錯: Argument 2 to "add" has incompatible type "str"; expected "int"
```
