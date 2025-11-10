# 🧮 Simple Python Calculator

A simple command-line calculator written in Python that performs basic arithmetic operations — addition, subtraction, multiplication, and division — based on user input.

## 📋 Features

- Accepts two numbers as input  
- Performs one of the following operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Handles invalid choices gracefully  
- Checks for division by zero  

## 💻 Usage

### 1. Run the program

```bash
python calculator.py
2. Example interaction
yaml
Copy code
Enter the 1st number: 10
Enter the 2nd number: 5
Enter your choice (+, -, *, /): *
Result: 50
3. Division by zero example
vbnet
Copy code
Enter the 1st number: 8
Enter the 2nd number: 0
Enter your choice (+, -, *, /): /
Error: Division by zero is not allowed.
🧠 Code Example
python
Copy code
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
choice = input("Enter your choice (+, -, *, /): ")

if choice == "-":
    print(a - b)
elif choice == "+":
    print(a + b)
elif choice == "*":
    print(a * b)
elif choice == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice")
🗂️ File Structure
bash
Copy code
calculator/
│
├── calculator.py   # Main program file
└── README.md       # Documentation
⚙️ Requirements
Python 3.x

🧑‍💻 Author
Created by [PARTH RAO] — a simple demo project for learning Python basics.

