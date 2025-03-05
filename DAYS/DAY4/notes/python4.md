# **Randomization & Python Lists** 🚀

Python provides the `random` module to perform **randomization** with lists, numbers, and sequences.

---

## **1️⃣ Randomizing Elements in a List**

### **a) Select a Random Item from a List**

Use `random.choice()` to pick a single random element.

```python
import random

fruits = ["apple", "banana", "cherry", "mango"]
random_fruit = random.choice(fruits)
print(random_fruit)
```

✅ **Output:** Randomly prints one fruit (e.g., `"banana"`).

---

### **b) Select Multiple Random Items**

Use `random.sample()` to get **N** unique random items.

```python
random_fruits = random.sample(fruits, 2)
print(random_fruits)
```

✅ **Output:** `['apple', 'mango']` (random selection)

---

### **c) Shuffle a List (Change Order Randomly)**

Use `random.shuffle()` to rearrange elements randomly.

```python
random.shuffle(fruits)
print(fruits)
```

✅ **Output:** The list order changes (e.g., `['mango', 'banana', 'apple', 'cherry']`).

---

## **2️⃣ Generating Random Numbers**

### **a) Generate a Random Integer**

```python
num = random.randint(1, 10)  # Random number between 1 and 10
print(num)
```

### **b) Generate a Random Float (Between 0 and 1)**

```python
num = random.random()  # Returns a float between 0.0 and 1.0
print(num)
```

### **c) Generate a Random Float in a Range**

```python
num = random.uniform(5, 10)  # Random float between 5 and 10
print(num)
```

---

## **3️⃣ Randomizing Index-Based Selection**

You can use `random.randrange()` to pick a random index.

```python
index = random.randrange(len(fruits))
print(fruits[index])
```

✅ **Output:** Random fruit selection based on index.

---

### **🔥 Summary**

- **Random selection:** `random.choice()`
- **Multiple selections:** `random.sample()`
- **Shuffle list:** `random.shuffle()`
- **Random integers:** `random.randint(start, end)`
- **Random floats:** `random.random()` or `random.uniform(start, end)`

### **Lists in Python** 🚀

A **list** in Python is an ordered, mutable (changeable) collection that can hold different data types.

---

## **1️⃣ Creating a List**

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 10, 3.14, True]
```

✅ Lists can contain **strings, numbers, booleans, or even other lists**.

---

## **2️⃣ Accessing Elements in a List**

### **a) Indexing (0-based)**

```python
print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: cherry (last element)
```

### **b) Slicing (Get a portion of the list)**

```python
print(fruits[0:2])  # Output: ['apple', 'banana']
print(fruits[:2])   # Output: ['apple', 'banana']
print(fruits[1:])   # Output: ['banana', 'cherry']
```

---

## **3️⃣ Modifying Lists**

### **a) Change a Value**

```python
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

### **b) Add Elements**

```python
fruits.append("mango")      # Adds at the end
fruits.insert(1, "orange")  # Adds at index 1
print(fruits)
```

### **c) Remove Elements**

```python
fruits.remove("apple")  # Removes by value
fruits.pop(1)           # Removes by index
del fruits[0]           # Deletes an element
fruits.clear()          # Removes all elements
```

---

## **4️⃣ Looping Through a List**

```python
for fruit in fruits:
    print(fruit)
```

Or using **enumerate()** to get index and value:

```python
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

## **5️⃣ List Methods**

| Method         | Description                    | Example                     |
| -------------- | ------------------------------ | --------------------------- |
| `append(x)`    | Add item at the end            | `fruits.append("mango")`    |
| `insert(i, x)` | Insert at index `i`            | `fruits.insert(1, "grape")` |
| `remove(x)`    | Remove first occurrence of `x` | `fruits.remove("apple")`    |
| `pop(i)`       | Remove item at index `i`       | `fruits.pop(2)`             |
| `sort()`       | Sort the list (ascending)      | `fruits.sort()`             |
| `reverse()`    | Reverse the list order         | `fruits.reverse()`          |
| `count(x)`     | Count occurrences of `x`       | `fruits.count("banana")`    |
| `index(x)`     | Find index of `x`              | `fruits.index("cherry")`    |

---

## **6️⃣ List Comprehension (Fast Way to Create Lists)**

```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

---

### **🔥 Summar_y**

- Lists are **mutable**, ordered collections.
- Supports **indexing, slicing, and looping**.
- Various **methods** for modification and searching.
- **List comprehension** makes creating lists efficient.

Let me know if you need more details! 🚀
