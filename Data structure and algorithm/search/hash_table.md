Hash table 觀念

第一步：建立一個空的 Hash 表
可以使用字典或是集合來建立 hash 表。

```python
# 建立一個空字典 (Hash Table)
scores = {}

# scores = dict()

print("目前的聯絡簿:", scores)
# 輸出: 目前的聯絡簿: {}
```

```python
set1 = set(nums1)
set2 = set(nums2)
```

第二步：新增資料 (Create)
現在我們要把學生的名字 (Key) 和分數 (Value) 寫進去。

口訣： 字典名[關鍵字] = 值

```python
# 新增三位學生的成績
scores["小明"] = 90
scores["小華"] = 85
scores["小美"] = 95

print("新增後的成績:", scores)
# 輸出: 新增後的成績: {'小明': 90, '小華': 85, '小美': 95}
```

第三步：快速查詢資料 (Read)
這是 Hash 表最強大的地方。不用從頭找，直接叫名字！

```python
# 1. 直接查詢 (如果確定名字存在)
print("小明的成績是:", scores["小明"])
# 輸出: 小明的成績是: 90

# 2. 安全查詢 (如果不確定名字在不在)
# 如果用 scores["大雄"] 會報錯 (KeyError)，因為大雄不在表裡。
# 所以我們用 .get() 方法，如果找不到，它會給一個預設值 (例如 None 或 "沒考")
print("大雄的成績是:", scores.get("大雄", "查無此人"))
# 輸出: 大雄的成績是: 查無此人
```

第四步：修改資料 (Update)
小華去複查考卷，發現老師改錯了，要加分。 在 Hash 表中，Key 是唯一的。如果您對同一個 Key 再次賦值，舊的資料就會被覆蓋。

```python
print("修改前小華:", scores["小華"])

# 直接覆蓋掉舊的分數
scores["小華"] = 88

print("修改後小華:", scores["小華"])
print("目前的表:", scores)
# 輸出: 目前的表: {'小明': 90, '小華': 88, '小美': 95}
```

第四步半：檢查資料是否存在
在做動作之前，通常會先問「這個人在不在名單裡？」

python 的查詢是查詢鍵存不存在，有的話，回傳值回來，不是查詢值，回傳鍵回來。

```python
student_name = "胖虎"

if student_name in scores:
    print(f"{student_name} 的成績是 {scores[student_name]}")
else:
    print(f"找不到 {student_name} 的資料")
```

第五步：刪除資料 (Delete)
小明轉學了，要把他的資料移除。

```python
# 使用 del 指令
del scores["小明"]

print("刪除小明後的表:", scores)
# 輸出: 刪除小明後的表: {'小華': 88, '小美': 95}

# 另一種方式：使用 .pop() (刪除同時還會把分數回傳給你)
removed_score = scores.pop("小美")
print(f"小美被刪除了，她原本考 {removed_score} 分")
```

第六步：遍歷資料 (Loop)
這是老師最常用的功能：把全班成績印出來，或者算平均分。

```python
# 先把資料補回來一點
scores = {'小華': 88, '小美': 95, '大雄': 60, '靜香': 92}

print("--- 全班成績單 ---")

# .items() 可以同時抓出 名字(key) 和 分數(value)
for name, score in scores.items():
    print(f"學生: {name}, 分數: {score}")

# 算平均分
total_score = sum(scores.values()) # .values() 只抓分數
average = total_score / len(scores)
print(f"全班平均: {average}")
```
