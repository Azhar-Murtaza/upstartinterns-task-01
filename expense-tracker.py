import csv
from datetime import datetime

expenses = []


# Add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")

    # Check date
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date!")
        return

    category = input("Enter category: ")

    # Check amount
    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0")
            return

    except ValueError:
        print("Invalid amount!")
        return

    # Store expense as dictionary
    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


# Show all expenses
def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\nDate\t\tCategory\tAmount")

    for expense in expenses:
        print(
            expense["date"],
            "\t",
            expense["category"],
            "\t",
            expense["amount"]
        )


# Calculate total spending by category
def total_by_category():

    totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    print("\nTotal Spending:")

    for category in totals:
        print(category, "=", totals[category])


# Save expenses to CSV
def save_to_csv():

    with open("expenses.csv", "w", newline="") as file:

        fieldnames = ["date", "category", "amount"]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(expenses)

    print("Expenses saved to expenses.csv")


# Main program
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total by Category")
    print("4. Save to CSV")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_by_category()

    elif choice == "4":
        save_to_csv()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")