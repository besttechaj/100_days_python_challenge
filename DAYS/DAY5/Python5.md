# **Loops and Iteration Types in Python**  

In Python, **iteration** refers to the process of executing a set of statements repeatedly. There are different ways to iterate over sequences, collections, or conditions.  

---

## **1. Types of Loops in Python**
Python provides two main types of loops for iteration:  

1. **`for` loop** – Used for iterating over a sequence (list, tuple, dictionary, set, or string).  
2. **`while` loop** – Runs as long as a condition remains `True`.  

---

## **2. Types of Iteration in Python**  

### **A. Definite Iteration (Fixed Number of Iterations)**
- Occurs when we know beforehand how many times the loop should execute.
- The `for` loop is mainly used for definite iteration.  

#### **Example:** Iterating over a list  
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
**Output:**  
```
apple  
banana  
cherry  
```

#### **Example:** Using `range()`  
```python
for i in range(5):
    print(i)
```
**Output:**  
```
0  
1  
2  
3  
4  
```

---

### **B. Indefinite Iteration (Unknown Number of Iterations)**
- Occurs when the number of iterations is not known in advance.
- The `while` loop is used for indefinite iteration.  

#### **Example:** User input loop  
```python
user_input = ""
while user_input != "exit":
    user_input = input("Enter something (type 'exit' to stop): ")
    print("You entered:", user_input)
```
- This loop runs until the user enters `"exit"`.

#### **Example:** Counting until a condition is met  
```python
x = 1
while x < 5:
    print(x)
    x += 1
```
**Output:**  
```
1  
2  
3  
4  
```

---

### **C. Iteration Over Different Data Structures**
Python allows iteration over various iterable objects:  

#### **1. Iterating Over a String**  
```python
for char in "Hello":
    print(char)
```
**Output:**  
```
H  
e  
l  
l  
o  
```

#### **2. Iterating Over a List**  
```python
numbers = [10, 20, 30]
for num in numbers:
    print(num)
```
**Output:**  
```
10  
20  
30  
```

#### **3. Iterating Over a Tuple**  
```python
tup = (1, 2, 3)
for item in tup:
    print(item)
```
**Output:**  
```
1  
2  
3  
```

#### **4. Iterating Over a Dictionary (Keys and Values)**  
```python
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, "->", value)
```
**Output:**  
```
name -> Alice  
age -> 25  
```

#### **5. Iterating Over a Set**  
```python
unique_numbers = {1, 2, 3}
for num in unique_numbers:
    print(num)
```

---

### **D. Using `enumerate()` for Index-Based Iteration**
The `enumerate()` function allows looping with an index.  

```python
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(index, ":", color)
```
**Output:**  
```
0 : red  
1 : green  
2 : blue  
```

---

### **E. Using `zip()` for Parallel Iteration**
`zip()` allows iterating over multiple sequences simultaneously.  

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, "is", age, "years old")
```
**Output:**  
```
Alice is 25 years old  
Bob is 30 years old  
Charlie is 35 years old  
```

---

### **F. Iteration Using List Comprehension**
List comprehensions provide a concise way to iterate and generate lists.  

```python
squares = [x**2 for x in range(5)]
print(squares)
```
**Output:**  
```
[0, 1, 4, 9, 16]  
```

---

### **G. Iterating Over Generators (`yield`)**
Generators allow memory-efficient iteration.  

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)
```
**Output:**  
```
1  
2  
3  
```

---

## **Conclusion**
Python supports multiple types of iteration, allowing flexibility based on the use case.  
- **Definite iteration (`for` loop)** is used when the number of iterations is known.  
- **Indefinite iteration (`while` loop)** is used when the number of iterations is unknown.  
- **Iteration can be done over strings, lists, tuples, dictionaries, sets, generators, and more.**  
- **Functions like `enumerate()`, `zip()`, and list comprehensions** make iteration more efficient.
