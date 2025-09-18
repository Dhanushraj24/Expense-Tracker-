# 📊 Expense Tracker (Python + MySQL)

A simple **command-line Expense Tracker** built with **Python** and **MySQL**. This project allows you to manage your personal expenses by adding, viewing, searching, updating, and deleting records efficiently.

---

## 🚀 Features

* ➕ **Add Expense** – Store new expense records with category, amount, and timestamp.
* 📜 **View All Expenses** – Display all stored expenses in a clean format.
* 🔍 **Search Expense by ID** – Find specific expense records quickly.
* ✏️ **Update Expense** – Modify existing records with new details.
* ❌ **Delete Expense** – Remove unwanted expense entries.
* 💰 **View Total Expenses** – Get the sum of all expenses for easy tracking.

---

## ⚙️ Setup & Installation

### 1. Install Requirements

Make sure you have Python installed. Then install the MySQL connector:

```bash
pip install mysql-connector-python
```

### 2. Setup MySQL Database

1. Open MySQL and create a new database:

   ```sql
   CREATE DATABASE expensedb;
   ```

2. The project will automatically create the `expenses` table if it does not exist:

   ```sql
   CREATE TABLE IF NOT EXISTS expenses (
       id INT AUTO_INCREMENT PRIMARY KEY,
       category VARCHAR(100) NOT NULL,
       amount DECIMAL(10,2) NOT NULL,
       date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

### 3. Connect Python to MySQL

Update the connection details in your script if needed:

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",          # your MySQL username
    password="password",  # your MySQL password
    database="expensedb"   # database name
)
```

---

## ▶️ How It Works (Procedure)

1. **Run the script**:

   ```bash
   python expense_tracker.py
   ```

2. **Menu Options**:

   * `1` → Add a new expense
   * `2` → View all expenses
   * `3` → Search expense by ID
   * `4` → Update existing expense
   * `5` → Delete expense
   * `6` → View total expenses
   * `7` → Exit program

3. **Example Flow**:

   * User selects `1` → Enters category & amount → Expense is saved in MySQL.
   * User selects `2` → Fetches and displays all expenses from DB.
   * User selects `6` → Shows total sum of expenses.

---

## 📂 Project Structure

```
📦 expense-tracker
 ┣ 📜 expense_tracker.py   # Main script
 ┣ 📜 README.md            # Documentation
```

---

## 🛠️ Tech Stack

* **Python** (for backend logic)
* **MySQL** (for database)

---

## 📌 Future Improvements

* Add expense filtering by date/category.
* Generate expense reports in CSV/Excel.
* Build a simple GUI with Tkinter or Flask.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to suggest new features or improvements.

---

## 📧 Contact

Created by **Dhanush** – If you like this project, give it a ⭐ on GitHub!
