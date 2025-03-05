# **Typecasting in Python**

Typecasting (also called **type conversion**) is the process of converting one data type into another. Python supports **two types of typecasting**:

1. **Implicit Typecasting (Automatic Conversion)**
2. **Explicit Typecasting (Manual Conversion)**

---

## **1. Implicit Typecasting (Automatic Conversion)**

Python automatically converts a smaller data type into a larger data type to avoid data loss.

### **Example:**

```python
a = 10      # int
b = 2.5     # float
c = a + b   # int + float → float

print(c)    # 12.5
print(type(c))  # <class 'float'>
```

📌 **Explanation:**

- `a` is an integer (`int`), and `b` is a floating point number (`float`).
- Python automatically converts `a` to `float` before performing the addition.

---

## **2. Explicit Typecasting (Manual Conversion)**

You can manually convert data types using **built-in functions**:

| Function     | Converts to           |
| ------------ | --------------------- |
| `int(x)`     | Integer               |
| `float(x)`   | Floating point number |
| `complex(x)` | Complex number        |
| `str(x)`     | String                |
| `list(x)`    | List                  |
| `tuple(x)`   | Tuple                 |
| `set(x)`     | Set                   |
| `dict(x)`    | Dictionary            |
| `bool(x)`    | Boolean               |

---

### **Examples of Explicit Typecasting**

#### **1. Converting to Integer (`int`)**

```python
x = "100"
y = int(x)  # String to int

print(y)  # 100
print(type(y))  # <class 'int'>
```

#### **2. Converting to Float (`float`)**

```python
x = "3.14"
y = float(x)  # String to float

print(y)  # 3.14
print(type(y))  # <class 'float'>
```

#### **3. Converting to String (`str`)**

```python
x = 123
y = str(x)  # Integer to string

print(y)  # "123"
print(type(y))  # <class 'str'>
```

#### **4. Converting to List (`list`)**

```python
x = "hello"
y = list(x)  # String to list

print(y)  # ['h', 'e', 'l', 'l', 'o']
```

#### **5. Converting to Tuple (`tuple`)**

```python
x = [1, 2, 3]
y = tuple(x)  # List to tuple

print(y)  # (1, 2, 3)
```

#### **6. Converting to Set (`set`)**

```python
x = "banana"
y = set(x)  # String to set (removes duplicates)

print(y)  # {'b', 'a', 'n'}
```

#### **7. Converting to Dictionary (`dict`)**

```python
x = [(1, "one"), (2, "two")]
y = dict(x)  # List of tuples to dictionary

print(y)  # {1: 'one', 2: 'two'}
```

#### **8. Converting to Boolean (`bool`)**

```python
print(bool(0))   # False
print(bool(1))   # True
print(bool(""))  # False (empty string)
print(bool("Hello"))  # True
```

---

### **Key Takeaways**

✅ **Implicit Typecasting** happens automatically (e.g., `int` → `float`).  
✅ **Explicit Typecasting** requires built-in functions (`int()`, `float()`, `str()`, etc.).  
✅ Some conversions may **cause errors** (e.g., converting `"abc"` to `int` fails).

---

## **PEMDASLR Rule in Python (Operator Precedence)**

Python follows the **PEMDASLR** rule to evaluate mathematical expressions. This rule defines the order in which operators are executed.

🔢 **PEMDASLR stands for:**  
📌 **P** – Parentheses `()`  
📌 **E** – Exponents `**`  
📌 **MD** – Multiplication `*` and Division `/` (Left to Right)  
📌 **AS** – Addition `+` and Subtraction `-` (Left to Right)  
📌 **LR** – Left to Right evaluation for operators with the same precedence

---

## **1. Order of Precedence in Python**

| Precedence  | Operator            | Description                                       |
| ----------- | ------------------- | ------------------------------------------------- |
| 1 (Highest) | `()`                | Parentheses                                       |
| 2           | `**`                | Exponentiation                                    |
| 3           | `*`, `/`, `//`, `%` | Multiplication, Division, Floor Division, Modulus |
| 4           | `+`, `-`            | Addition, Subtraction                             |
| 5 (Lowest)  | `=`                 | Assignment                                        |

---

## **2. Example Demonstrations**

### **A. Parentheses (`()`) First**

```python
result = (5 + 3) * 2
print(result)  # 16 (Addition first, then multiplication)
```

### **B. Exponentiation (`**`) Next\*\*

```python
result = 2 ** 3 * 2
print(result)  # 16 (Exponentiation first: 2³ = 8, then multiplication: 8 * 2)
```

### **C. Multiplication and Division (`*`, `/`, `//`, `%`)**

```python
result = 10 + 5 * 2
print(result)  # 20 (Multiplication first: 5 * 2 = 10, then addition)

result = 10 / 2 + 3
print(result)  # 8.0 (Division first: 10 / 2 = 5, then addition)

result = 10 // 3
print(result)  # 3 (Floor division: 10 divided by 3, rounded down)

result = 10 % 3
print(result)  # 1 (Modulus: Remainder of 10 divided by 3)
```

### **D. Addition and Subtraction (`+`, `-`)**

```python
result = 10 - 5 + 2
print(result)  # 7 (Left to right: 10 - 5 = 5, then 5 + 2 = 7)
```

---

## **3. Left to Right (LR) Rule**

Operators with the **same precedence** are evaluated **from left to right**.

### **Example :**

```python
result = 10 - 2 + 3
# Left to right: (10 - 2) = 8, then 8 + 3 = 11
print(result)  # 11
```

🚨 **Exception: Exponentiation (`**`) follows Right to Left order\*\*

```python
result = 2 ** 3 ** 2
# Right to left: (3 ** 2) = 9, then 2 ** 9 = 512
print(result)  # 512
```

---

### **4. Operator Precedence Table Example**

| Expression    | Evaluation Order           | Result |
| ------------- | -------------------------- | ------ |
| `5 + 3 * 2`   | `3 * 2 = 6`, then `5 + 6`  | `11`   |
| `(5 + 3) * 2` | `5 + 3 = 8`, then `8 * 2`  | `16`   |
| `2 ** 3 * 2`  | `2³ = 8`, then `8 * 2`     | `16`   |
| `10 / 2 + 3`  | `10 / 2 = 5`, then `5 + 3` | `8.0`  |
| `10 - 2 + 3`  | `10 - 2 = 8`, then `8 + 3` | `11`   |

---

### **5. Summary**

✔ **Parentheses** have the highest priority.  
✔ **Exponentiation** (`**`) is evaluated **right to left**.  
✔ **Multiplication, Division, Modulus, and Floor Division** have equal priority and are evaluated **left to right**.  
✔ **Addition and Subtraction** are the lowest in precedence (except assignment).

-----

# **f-string in Python (Formatted String Literals)**

An **f-string** (formatted string literal) is a powerful way to format strings in Python. It was introduced in **Python 3.6** and allows embedding expressions inside string literals using `{}`.

---

## **1. Basic Syntax**

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

🔹 **Output:**  

```
My name is Alice and I am 25 years old.
```

---

## **2. Expressions Inside f-strings**

You can perform **calculations** inside `{}`:

```python
x = 10
y = 5
print(f"Sum: {x + y}, Product: {x * y}")
```

🔹 **Output:**  

```
Sum: 15, Product: 50
```

---

## **3. Calling Functions in f-strings**

```python
def greet(name):
    return f"Hello, {name}!"

print(f"{greet('Bob')}")
```

🔹 **Output:**  

```
Hello, Bob!
```

---

## **4. Formatting Numbers**

```python
pi = 3.1415926535
print(f"Pi rounded: {pi:.2f}")  # 2 decimal places
print(f"Pi scientific: {pi:.3e}")  # Scientific notation
```

🔹 **Output:**  

```
Pi rounded: 3.14
Pi scientific: 3.142e+00
```

---

## **5. Padding & Alignment**

| Alignment | Symbol | Example |
|-----------|--------|---------|
| Left align | `<` | `{value:<10}` |
| Right align | `>` | `{value:>10}` |
| Center align | `^` | `{value:^10}` |

```python
name = "Bob"
print(f"{name:<10} Left")   # Left align
print(f"{name:>10} Right")  # Right align
print(f"{name:^10} Center") # Center align
```

🔹 **Output:**  

```
Bob        Left
       Bob Right
   Bob    Center
```

---

## **6. Using f-strings with Dictionaries**

```python
person = {"name": "Charlie", "age": 30}
print(f"Name: {person['name']}, Age: {person['age']}")
```

🔹 **Output:**  

```
Name: Charlie, Age: 30
```

---

## **7. Using f-strings with Lists**

```python
fruits = ["Apple", "Banana", "Cherry"]
print(f"My favorite fruit is {fruits[0]}.")
```

🔹 **Output:**  

```
My favorite fruit is Apple.
```

---

## **8. Nesting f-strings**

```python
a, b = 5, 10
print(f"Sum of {a} and {b} is {f'{a + b}'}")
```

🔹 **Output:**  

```
Sum of 5 and 10 is 15
```

---

## **9. Using f-strings for Debugging (Python 3.8+)**

Python 3.8 introduced the `=` feature to print variable names along with values.

```python
x = 42
print(f"{x=}")
```

🔹 **Output:**  

```
x=42
```

---

## **10. Multi-line f-strings**

You can use triple quotes (`"""` or `'''`) for multi-line f-strings:

```python
name = "Alice"
age = 25
print(f"""
Name: {name}
Age: {age}
""")
```

🔹 **Output:**  

```
Name: Alice
Age: 25
```

---

### **🛠 Advantages of f-strings**

✅ **Faster** than `.format()` and `%` formatting  
✅ **More readable & concise**  
✅ **Can evaluate expressions directly**  

