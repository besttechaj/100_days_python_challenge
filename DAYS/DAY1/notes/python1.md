# **Python Introduction Notes**

## **1. What is Python?**

- Python is a high-level, interpreted programming language.
- It is known for its simple syntax, readability, and versatility.
- Used in web development, data science, AI/ML, automation, and more.

## **2. Features of Python**

✅ Easy to learn and use  
✅ Open-source and free  
✅ Interpreted language (no need to compile)  
✅ Dynamically typed (no need to declare variable types)  
✅ Large standard library and community support  
✅ Cross-platform (runs on Windows, Mac, Linux)

## **3. Installing Python**

- Download and install Python from [python.org](https://www.python.org).
- Check installation:

  ```sh
  python --version
  ```

- Use **pip** (Python package manager) for installing libraries:

  ```sh
  pip install numpy
  ```

## **4. Writing and Running Python Code**

- Python scripts have a `.py` extension.
- Run a Python script:

  ```sh
  python script.py
  ```

- Use the interactive shell (REPL) by running `python` in the terminal.

## **5. Python Syntax Basics**

### **Variables and Data Types**

```python
x = 10        # Integer
y = 3.14      # Float
name = "John" # String
is_valid = True  # Boolean
```

### **Basic Input and Output**

```python
name = input("Enter your name: ")  # Taking user input
print("Hello, " + name)            # Printing output
```

### **Operators in Python**

- Arithmetic: `+`, `-`, `*`, `/`, `%`, `**` (exponent), `//` (floor division)
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`

### **Conditional Statements**

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
```

### **Loops in Python**

#### **For Loop**

```python
for i in range(5):  # Loops from 0 to 4
    print(i)
```

#### **While Loop**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### **Functions in Python**

```python
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
```

### **Lists (Arrays in Python)**

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Accessing first element
numbers.append(6)  # Adding an element
print(numbers)
```

### **Dictionaries (Key-Value Pairs)**

```python
student = {"name": "Alice", "age": 20, "city": "New York"}
print(student["name"])  # Access value by key
student["age"] = 21     # Updating a value
```

## **6. Python Libraries & Modules**

- Python has built-in modules and external libraries for various tasks.
- Example: Using the `math` module

  ```python
  import math
  print(math.sqrt(16))  # Output: 4.0
  ```

- Popular Python libraries:
  - **NumPy** (scientific computing)
  - **Pandas** (data analysis)
  - **Matplotlib** (visualization)
  - **TensorFlow** (AI & ML)

## **7. Object-Oriented Programming (OOP) in Python**

```python
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

p1 = Person("Alice", 25)
p1.greet()
```

## **8. Exception Handling (Error Handling)**

```python
try:
    x = 10 / 0  # This will cause an error
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution complete.")
```

## **9. File Handling**

```python
# Writing to a file
with open("test.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
```

## **10. Python and Data Science/AI**

- Libraries like **NumPy**, **Pandas**, **Matplotlib**, and **Scikit-learn** are used for data analysis and machine learning.
- Example: Using NumPy for arrays

  ```python
  import numpy as np
  arr = np.array([1, 2, 3, 4, 5])
  print(arr * 2)  # Multiply each element by 2
  ```

## **Variables in Python**

## **What is a Variable?**

A variable in Python is used to store data values. Unlike other programming languages, you don’t need to declare the type of a variable explicitly because Python is dynamically typed.

### **Declaring Variables**

```python
x = 10        # Integer
y = 3.14      # Float
name = "John" # String
is_valid = True  # Boolean
```

Python automatically determines the data type based on the assigned value.

---

## **Variable Naming Rules**

✅ Must start with a letter (a-z, A-Z) or underscore (_)  
✅ Can contain letters, digits (0-9), and underscores (_)  
✅ Case-sensitive (`age` and `Age` are different variables)  
✅ Cannot be a Python keyword (e.g., `if`, `for`, `while`, `def`, etc.)

### **Valid Variable Names**

```python
my_var = 5
_age = 25
userName = "Alice"
```

### **Invalid Variable Names (Will Cause Errors)**

```python
2name = "John"    # ❌ Cannot start with a number
my-var = 10       # ❌ Cannot use hyphens
class = "Python"  # ❌ Cannot use a Python keyword
```

---

## **Dynamic Typing**

Python allows you to change the data type of a variable at any time.

```python
x = 10     # x is an integer
x = "Hello"  # x is now a string
```

---

## **Multiple Variable Assignment**

Python allows multiple variables to be assigned in a single line.

```python
a, b, c = 1, 2, 3
print(a, b, c)  # Output: 1 2 3
```

You can also assign the same value to multiple variables.

```python
x = y = z = 100
print(x, y, z)  # Output: 100 100 100
```

---

## **Variable Types in Python**

| Data Type  | Example                                 |
| ---------- | --------------------------------------- |
| Integer    | `x = 10`                                |
| Float      | `y = 3.14`                              |
| String     | `name = "John"`                         |
| Boolean    | `is_valid = True`                       |
| List       | `numbers = [1, 2, 3]`                   |
| Tuple      | `coordinates = (10, 20)`                |
| Dictionary | `person = {"name": "Alice", "age": 25}` |
| Set        | `unique_numbers = {1, 2, 3, 4, 5}`      |

---

## **Checking Variable Type**

You can check the type of a variable using `type()`.

```python
x = 10
print(type(x))  # Output: <class 'int'>

y = "Hello"
print(type(y))  # Output: <class 'str'>
```

---

## **Deleting Variables**

You can delete a variable using `del`.

```python
x = 10
del x
print(x)  # ❌ This will cause an error because x is deleted
```

---

This covers the basics of variables in Python. Let me know if you have any questions! 🚀
