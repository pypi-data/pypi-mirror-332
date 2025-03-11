**BuildEasy** is a Python package that dynamically transforms Python files into class instances. It enhances modularity by allowing runtime modifications, automatic method injection, and plugin-based module loading. Here's a breakdown of its key features and usage:

---

### **Key Features**
1. **Automatic File-to-Class Conversion**  
   - Python files (`.py`) are converted into class instances when subclassed from `FileAsClass`.
   
2. **Dynamic Method Injection**  
   - Methods can be added dynamically, including static methods, class methods, or instance methods.
   
3. **Caching for Performance**  
   - Prevents redundant transformations by caching instances.

4. **State Persistence**  
   - Supports saving and loading instances using `pickle` for state management.

5. **Plugin System**  
   - Scans directories for Python files and loads them dynamically as modules.

6. **Custom Attribute Resolution**  
   - Overrides attribute lookups to enable flexible behavior.

7. **Live Code Modification**  
   - The `Adaptor` class allows real-time updates to functions and classes, even modifying source files directly.
   
8. **Find and Replace Functionality**  
   - Enables targeted string replacements in source files for dynamic code evolution.

---

### **How It Works**
#### **1. Converting a Python File into a Class**
By subclassing `FileAsClass`, a module (`my_module.py`) is transformed into a class instance:

```python
from buildeasy import FileAsClass

class MyModule(FileAsClass):
    def __init__(self, name="buildeasy"):
        self.name = name

    def greet(self):
        return f"Hello from {self.name}!"
```

Accessing the module (`main.py`):
```python
import my_module

print(my_module.greet())  # Outputs: Hello from my_module.py!
print(my_module.name)  # Outputs: buildeasy
```

---

#### **2. Adding Methods Dynamically**
```python
def farewell():
    return "Goodbye!"

my_module.add_method("farewell", farewell)
print(my_module.farewell())  # Outputs: Goodbye!
```

---

#### **3. Saving and Loading Instances**
```python
my_module.save("module_state.pkl")
loaded_instance = my_module.load("module_state.pkl")
```

---

#### **4. Scanning for Plugins**
```python
my_module.scan("plugins/")
```

---

#### **5. Live Code Modification**
Using the `Adaptor` class, you can update functions and classes in real time:
```python
from buildeasy import Adaptor

new_function_code = """
def greet():
    return "Hello from the modified function!"
"""

Adaptor.update("my_module", "greet", new_function_code)
print(my_module.greet())  # Outputs: Hello from the modified function!
```

---

#### **6. Finding and Replacing Code in Source Files**
```python
Adaptor.find_and_replace("my_module", "Hello", "Hi")
```
This will replace all instances of "Hello" with "Hi" in `my_module.py`.

### **7. Running Code:**
To run the code, you can use the `run_code` function:
```python
Adaptor.run_code("my_module", "greet()")  # Outputs: Hello from my_module.py!
```

---

### **Why Use BuildEasy?**
- Makes Python files behave like objects with dynamic behaviors.
- Eliminates redundant file imports by turning them into reusable instances.
- Enables plugin-like extensibility by auto-loading modules.
- Allows live updates to Python code without restarting applications.

It's especially useful for **dynamic applications, plugin-based architectures, or frameworks** that require runtime modifications and flexible module management. 🚀