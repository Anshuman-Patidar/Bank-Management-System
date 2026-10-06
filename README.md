# 🏦 Python Banking Management System

A simple **console-based Banking Management System** built using **Python and Object-Oriented Programming (OOP)** concepts.

This project allows customers to create a bank account, log in using their ID and password, view account information, check their balance, deposit money, and withdraw money.

It is designed as a **beginner-level Python project** to practice classes, objects, encapsulation, methods, lists, loops, conditional statements, and basic authentication logic.

---

## 📌 Features

- 🏦 Bank account creation
- 👤 Customer signup
- 🔐 Customer login with ID and password
- 🔑 Password verification with limited attempts
- 📄 Display bank and customer information
- 💰 Balance enquiry
- ➕ Deposit money
- ➖ Withdraw money
- 🚫 Insufficient balance validation
- 🔄 Menu-driven banking system
- 👥 Multiple customer objects
- 🔒 Private attributes for balance and password

---

## 🛠️ Technologies Used

- **Python 3**
- Object-Oriented Programming (OOP)
- Python `match-case`
- Lists
- Loops
- Conditional Statements
- Encapsulation
- Functions

---

## 🧠 OOP Concepts Used

This project was created to practice the following Python OOP concepts:

### 1. Class

The `Bank` class represents a bank customer account.

```python
class Bank:
    ...
```

### 2. Object

Each customer is represented by a separate object.

```python
c1 = Bank('aman', 1, 1, 1234.5, 'aman@123')
c2 = Bank('anshuman', 2, 2, 1234.5, 'anshuman@123')
```

### 3. Constructor

The `__init__()` method initializes customer account information.

```python
def __init__(self, name, ACC_NO, cid, __bankBalance, __password):
    self.name = name
    self.ACC_NO = ACC_NO
    self.id = cid
    self.__bankBalance = __bankBalance
    self.__password = __password
```

### 4. Encapsulation

Bank balance and password are stored using private attributes.

```python
self.__bankBalance
self.__password
```

This helps demonstrate the concept of **data hiding** in Python.

### 5. Methods

Different banking operations are implemented using methods:

- `Bank_info()`
- `Balance_enquiry()`
- `Deposit()`
- `Withdraw()`
- `match_password()`

---

## 📂 Project Structure

```text
Python-Banking-System/
│
├── bank.py
└── README.md
```

> `bank.py` contains the complete banking application.

---

## 🚀 How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Python-Banking-System.git
```

### Step 2: Open the Project

```bash
cd Python-Banking-System
```

### Step 3: Run the Python Program

```bash
python bank.py
```

---

## 💻 How the Application Works

When the program starts, the user gets the following options:

```text
1 : Signup
2 : Login
3 : Exit
```

### 👤 Signup

The user enters:

- Name
- Account Number
- Customer ID
- Initial Bank Balance
- Password

Example:

```text
enter the name anshuman
enter the account number 2
enter the id number 2
enter the bank Balance 1234.5
enter the password anshuman@123
```

The new customer is then added to the customer list.

---

### 🔐 Login

The customer logs in using their ID.

The application then verifies the password.

The login system allows a limited number of attempts.

After successful login, the customer gets access to the banking menu.

---

## 🏦 Banking Menu

After login, the customer can select:

```text
1 for Bank Information
2 for Bank Balance Enquiry
3 for Bank Deposit
4 for Withdraw
5 for Exit
```

### 1️⃣ Bank Information

Displays information such as:

- Bank name
- IFSC code
- Branch
- Customer name
- Account number
- Customer ID

### 2️⃣ Balance Enquiry

Displays the customer's current bank balance.

### 3️⃣ Deposit

The customer can enter an amount to deposit.

The amount is added to the existing balance.

### 4️⃣ Withdraw

The customer can withdraw money if sufficient balance is available.

The application checks:

```text
Available Balance >= Withdrawal Amount
```

### 5️⃣ Exit

Ends the banking menu.

---

## 📸 Example Output

```text
1 : Signup
2 : Login
3 : Exit

Enter the Choice: 2

limit=3, enter the Id: 2

limit=3, enter the password: anshuman@123

-------------------------------------

1 for Bank Information
2 for Bank Balance Enquiry
3 for Bank Deposit
4 for Withdraw
5 for Exit
```

---

## 🔒 Validation

The project includes basic validation for:

- Invalid customer ID
- Invalid password
- Limited password attempts
- Invalid deposit amount
- Invalid withdrawal amount
- Insufficient account balance

---

## 🎯 Learning Objectives

The main purpose of this project is to understand how Python OOP concepts can be used to build a small real-world application.

Through this project, I practiced:

- Creating classes and objects
- Constructors
- Instance variables
- Private attributes
- Encapsulation
- Methods
- Functions
- Lists of objects
- Loops
- Conditional statements
- `match-case`
- Basic authentication logic
- Menu-driven applications

---

## 🔮 Future Improvements

The current project uses an **in-memory list** as a local customer database. The following features can be added in future versions:

- 🗄️ SQLite/MySQL database
- 🔐 Password hashing
- 💳 Transaction history
- 📱 Better user interface
- 🧾 Account statement generation
- 💰 Transfer money between accounts
- 👨‍💼 Admin login
- 🗑️ Delete/close account
- ✏️ Update customer information
- 🌐 Convert the project into a Django REST API
- ⚛️ Add a React frontend

---

## ⚠️ Disclaimer

This is an **educational project** created for learning Python and Object-Oriented Programming.

It is **not intended for real banking or financial transactions**.

---

## 👨‍💻 Author

**Anshuman Patidar**

BCA Student | Python & Django Developer

### Skills

- Python
- Django
- React.js
- C
- C++

---

## ⭐ If You Like This Project

If you find this project useful for learning Python OOP, consider giving the repository a ⭐ star.

```text
Made with Python 🐍
```
