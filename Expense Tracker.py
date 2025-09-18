import mysql.connector
from datetime import datetime

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",              # change if needed
    password="Dhanush2003@",  # change if needed
    database="expensedb"      # database must exist
)

mycursor = mydb.cursor()

# Create table if not exists
mycursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(100) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# ================= Functions =================

# Add Expense
def add_expense():
    category = input("Enter Category (Food, Clothes, Travel, Online Orders, etc...): ")
    amount = float(input("Enter Amount: "))
    q = "INSERT INTO expenses (category, amount, date) VALUES (%s, %s, %s)"
    data = (category, amount, datetime.now())
    mycursor.execute(q, data)
    mydb.commit()
    print("Expense Added Successfully!")

# View All Expenses
def view_expenses():
    q = "SELECT * FROM expenses"
    mycursor.execute(q)
    data = mycursor.fetchall()
    count = mycursor.rowcount
    print(f"Total Expenses Records: {count}")
    for (eid, category, amount, date) in data:
        print(f"ID: {eid}, Category: {category}, Amount: {amount}, Date: {date}")
        print("----------------------------------")

# Search Expense by ID
def search_expense():
    eid = int(input("Enter Expense ID to Search: "))
    q = "SELECT * FROM expenses WHERE id=%s"
    mycursor.execute(q, (eid,))
    data = mycursor.fetchall()
    if data:
        print("Expense Record Found:")
        for (eid, category, amount, date) in data:
            print(f"ID: {eid}, Category: {category}, Amount: {amount}, Date: {date}")
    else:
        print("Record Not Found")

# Update Expense
def update_expense():
    eid = int(input("Enter Expense ID to Update: "))
    q = "SELECT * FROM expenses WHERE id=%s"
    mycursor.execute(q, (eid,))
    data = mycursor.fetchall()
    if data:
        print("Record Found. Enter new details:")
        category = input("Enter New Category: ")
        amount = float(input("Enter New Amount: "))
        q = "UPDATE expenses SET category=%s, amount=%s WHERE id=%s"
        mycursor.execute(q, (category, amount, eid))
        mydb.commit()
        print("Expense Updated Successfully!")
    else:
        print("Record Not Found")

# Delete Expense
def delete_expense():
    eid = int(input("Enter Expense ID to Delete: "))
    q = "SELECT * FROM expenses WHERE id=%s"
    mycursor.execute(q, (eid,))
    data = mycursor.fetchall()
    if data:
        confirm = input("Are you sure you want to DELETE this record (Y/N)? ")
        if confirm.upper() == "Y":
            q = "DELETE FROM expenses WHERE id=%s"
            mycursor.execute(q, (eid,))
            mydb.commit()
            print("Expense Deleted Successfully!")
    else:
        print("Record Not Found")

# Show Total Expenses
def total_expenses():
    q = "SELECT SUM(amount) FROM expenses"
    mycursor.execute(q)
    total = mycursor.fetchone()[0]
    print(f"Total Expenses: {total if total else 0}")

# ================= Menu =================
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense by ID")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. View Total Expenses")
    print("7. Exit")
    print("============================")

    choice = int(input("Enter Choice (1-7): "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        search_expense()
    elif choice == 4:
        update_expense()
    elif choice == 5:
        delete_expense()
    elif choice == 6:
        total_expenses()
    elif choice == 7:
        mydb.close()
        print("Exiting Expense Tracker... Have a great day!")
        break
    else:
        print("Invalid Choice! Please enter 1-7.")
