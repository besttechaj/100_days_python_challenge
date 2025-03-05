# **Control Flow and Logical Operators in Python** 🚀

## **1️⃣ Control Flow in Python**

Control flow determines how Python executes statements and makes decisions.

### **a) Conditional Statements (if, elif, else)**

Used for decision-making.

```python
x = 10

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

✅ **Output:** `Positive`

---

#### **b) Loops (for, while)**

Used to repeat code.

🔹 **For Loop** (Iterates over sequences)

```python
for i in range(5):
    print(i)
```

✅ **Output:** `0 1 2 3 4`

🔹 **While Loop** (Repeats while a condition is true)

```python
x = 5
while x > 0:
    print(x)
    x -= 1
```

✅ **Output:** `5 4 3 2 1`

---

#### **c) Loop Control Statements**

- `break` → Exits the loop early
- `continue` → Skips the current iteration
- `pass` → Placeholder for future code

```python
for i in range(5):
    if i == 2 or i == 4:
        continue  # Skips 2,4
    print(i)
```

✅ **Output:** `0 1 3`

---

### **2️⃣ Logical Operators in Python**

Logical operators are used to combine conditional statements.

| Operator | Description                            | Example                       |
| -------- | -------------------------------------- | ----------------------------- |
| `and`    | True if both conditions are True       | `(5 > 2) and (10 > 5) → True` |
| `or`     | True if at least one condition is True | `(5 > 10) or (10 > 5) → True` |
| `not`    | Reverses the condition                 | `not (5 > 2) → False`         |

```python
x = 5
y = 10

print(x > 2 and y < 20)  # True
print(x > 10 or y < 20)  # True
print(not (x > 2))       # False
```

---

### **🔥 Summary**

- **Control Flow:** `if-elif-else`, loops (`for`, `while`), loop control (`break`, `continue`, `pass`).
- **Logical Operators:** `and`, `or`, `not` for decision-making.

Let me know if you need examples or further explanation! 🚀
