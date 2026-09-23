# 🛠️ Multi-Utility Toolkit

A **menu-driven Python utility application** that combines multiple useful operations into a single program.

The project demonstrates practical usage of Python's built-in modules such as **`datetime`**, **`time`**, **`math`**, **`random`**, **`uuid`**, and **`string`**, along with a custom file-handling module.

---

## 📌 Overview

The **Multi-Utility Toolkit** provides a collection of utilities through an interactive command-line interface.

Instead of creating separate programs for different tasks, this project brings multiple operations together under one menu-driven application.

### Main Modules

```text
1. Date & Time Operations
2. Mathematical Operations
3. Random Data Generation
4. UUID Generation
5. File Operations
6. Module Attribute Exploration
7. Exit
```

The main program continuously displays the menu until the user selects the **Exit** option.

---

## ✨ Features

### 📅 1. Date & Time Operations

The toolkit provides several date and time utilities:

* Display current date and time
* Calculate the difference between two dates
* Create a custom date and time
* Stopwatch
* Countdown timer

The project uses Python's `datetime` and `time` modules for these operations.

---

### 🧮 2. Mathematical Operations

The mathematical section provides:

* Factorial calculation
* Compound interest calculation
* Trigonometric calculations
* Area calculation for different geometric shapes

Supported shapes include:

* Square
* Circle
* Rectangle
* Triangle

The project uses Python's `math` module for mathematical functions such as factorial, power, radians, trigonometric functions, and π.

---

### 🎲 3. Random Data Generation

The random-data section includes:

* Random number generation
* Random list generation
* Random password generation
* Random OTP generation

The toolkit uses the `random` and `string` modules to generate different types of random data.

---

### 🆔 4. UUID Generation

The UUID section generates unique identifiers using Python's `uuid` module.

The project demonstrates:

```python
uuid.uuid4()
uuid.uuid1()
```

These provide examples of different UUID generation methods.

---

### 📁 5. File Operations

The toolkit integrates a custom module named:

```text
file_module.py
```

The file-management section provides:

* Create a new file
* Write to a file
* Read from a file
* Append data to a file

These functions are imported into the main program using:

```python
from file_module import *
```

The file operations are therefore separated from the main application logic.

---

### 🔍 6. Module Attribute Exploration

The project also demonstrates Python's `dir()` function.

The user can enter a module name and explore its available attributes.

```python
dir(module_name)
```

This section is intended to demonstrate Python module inspection.

---

## 🏗️ Project Structure

A recommended project structure is:

```text
Multi-Utility-Toolkit/
│
├── main.py
├── file_module.py
└── README.md
```

### `main.py`

Contains the main menu and the different utility operations.

### `file_module.py`

Contains the custom file-handling functions.

### `README.md`

Contains project documentation and usage information.

---

## 🔄 Application Flow

```text
                    ┌─────────────────────┐
                    │   Multi-Utility     │
                    │      Toolkit        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Main Menu        │
                    └──────────┬──────────┘
                               │
          ┌────────────┬───────┼────────┬─────────────┐
          ▼            ▼       ▼        ▼             ▼
       Date/Time      Math   Random    UUID        Files
          │            │       │        │             │
          ▼            ▼       ▼        ▼             ▼
      Operations   Calculations Data   UUIDs      File Handling
                              
                               │
                               ▼
                    Module Attribute
                       Exploration
                               │
                               ▼
                             Exit
```

---

## 🧰 Technologies & Modules

| Technology / Module | Purpose                           |
| ------------------- | --------------------------------- |
| Python              | Core programming language         |
| `datetime`          | Date and time operations          |
| `time`              | Countdown and time delay          |
| `math`              | Mathematical calculations         |
| `random`            | Random data generation            |
| `uuid`              | Unique identifier generation      |
| `string`            | Characters for passwords and OTPs |
| Custom Module       | File operations                   |
| `dir()`             | Module attribute exploration      |

---

## ▶️ Getting Started

### Prerequisites

Make sure Python 3 is installed.

Check your Python version:

```bash
python --version
```

---

### Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd Multi-Utility-Toolkit
```

---

### Run the Application

```bash
python main.py
```

The application will display the main menu:

```text
WELCOME TO MULTI-UTILITY TOOLKIT

1. DATETIME AND TIME OPERATION
2. MATHEMATICAL OPERATION
3. RANDOM DATA GENERATION
4. GENERATE UNIQUE IDENTIFIER (UUID)
5. FILE OPERATIONS
6. EXPLORE MODULE ATTRIBUTE (DIR())
7. EXIT
```

---

## 💡 Example Usage

### Example 1 — Current Date & Time

```text
Choose an option: 1

1. DISPLAY CURRENT TIME AND DATE
2. CALCULATE DIFFERENCE BETWEEN TWO TIME/DATE
3. FORMAT DATE INTO CUSTOM DATE
4. STOPWATCH
5. COUNTDOWN
6. BACK TO MAIN MENU

Enter the choice: 1
```

Example output:

```text
TODAY DATE AND TIME IS :: 2026-09-23 11:30:25
```

---

### Example 2 — Factorial

```text
Enter the choice: 2

1. CALCULATE FACTORIAL
2. COMPOUND INTEREST
3. TRIGNOMETRIC CALCULATIONS
4. AREA OF GEOMETRIC SHAPES
5. BACK TO MAIN MENU

Enter the choice: 1
Input the number: 5
```

Output:

```text
Factorial of number is: 120
```

---

### Example 3 — Random Password

```text
Enter the choice: 3

3. CREATE RANDOM PASSWORD

Enter the length of password: 10
```

Example output:

```text
aK7pQ2xL9m
```

---

### Example 4 — UUID

Selecting the UUID option generates UUID values using the Python `uuid` module.

```text
using uuid4: 550e8400-e29b-41d4-a716-446655440000
using uuid1: ...
```

---

### Example 5 — File Operations

The file menu provides:

```text
1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
5. Back to main menu
```

The functions are provided by the custom `file_module.py` module.

---

## 📚 Python Concepts Demonstrated

This project provides practical implementation of:

* `while` loops
* `match-case`
* Functions
* User input
* Conditional statements
* Nested menus
* Exception handling
* File handling
* Custom modules
* Module importing
* `datetime`
* `timedelta`
* `time.sleep()`
* Mathematical functions
* Random data generation
* UUID generation
* String operations
* `dir()`
* `if __name__ == "__main__"`

---

## 🧩 Custom File Module

The custom file module contains functions for:

```python
create_file()
write_file()
read_file()
apppend_file()
```

The main program imports these functions with:

```python
from file_module import *
```

This demonstrates how functionality can be separated into a reusable Python module.

> **Note:** The current function name is `apppend_file()`. If you want conventional spelling, rename it to `append_file()` in both `file_module.py` and `main.py`.

---

## 🎯 Learning Objectives

The main purpose of this project is to gain practical experience with Python's standard library and combine multiple concepts into one application.

After completing this project, you should have practical experience with:

1. Python standard modules
2. Menu-driven applications
3. Date and time manipulation
4. Mathematical calculations
5. Random data generation
6. UUID generation
7. File handling
8. Custom modules
9. Module inspection
10. User-input-based programs

---

## 🚀 Future Improvements

Possible improvements for future versions include:

* Input validation
* Better exception handling
* Cleaner menu navigation
* Separate modules for each utility
* Improved password generation
* More mathematical operations
* More geometric shapes
* File deletion and renaming
* Improved `dir()` module exploration
* Cleaner user interface
* Logging and error reporting

---

## 📌 Project Highlights

```text
✓ Menu-Driven Application
✓ Multiple Python Standard Modules
✓ Date & Time Utilities
✓ Mathematical Utilities
✓ Random Data Generation
✓ UUID Generation
✓ Custom File Module
✓ File Handling
✓ Module Exploration
✓ User Input
```

---

## 👨‍💻 Author

**Sanjay Kushwaha**

Python Learning & Utility Project

---

## 📄 License

This project is created for **educational and learning purposes**.

You are free to study, modify, and extend the project for your own learning.
