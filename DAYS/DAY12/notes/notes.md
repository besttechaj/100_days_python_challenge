# scopes

## In Python, **scope** refers to the region of a program where a **variable is recognized and can be used**. It determines the visibility and lifetime of a variable. There are **four types of scope** in Python, which follow the **LEGB Rule**

---

### 🔁 LEGB Rule (Local, Enclosing, Global, Built-in)

#### 1. **Local (L):**

- Defined inside a function.
- Only accessible within that function.

```python
def my_func():
    x = 10  # local scope
    print(x)

my_func()
# print(x)  # Error: x is not defined
```

---

#### 2. **Enclosing (E):**

- In nested functions, the inner function has access to variables of the outer (enclosing) function.

```python
def outer():
    y = 20  # Enclosing scope

    def inner():
        print(y)  # Can access y from enclosing scope

    inner()

outer()
```

---

#### 3. **Global (G):**

- Defined at the top level of a script or module.
- Accessible throughout the file.

```python
z = 30  # Global scope

def show():
    print(z)

show()
```

To **modify** a global variable inside a function, use the `global` keyword:

```python
count = 0

def increase():
    global count
    count += 1

increase()
print(count)
```

---

#### 4. **Built-in (B):**

- Names that are built into Python (e.g., `len`, `range`, `print`).

```python
print(len("Python"))  # len is a built-in function
```

---

### 🔐 Variable Resolution Order

When you access a variable, Python looks for it in this order:

1. **Local**
2. **Enclosing**
3. **Global**
4. **Built-in**

If Python can't find it in any of these, you get a `NameError`.

---

Would you like a visual diagram or a small quiz to test your understanding?
