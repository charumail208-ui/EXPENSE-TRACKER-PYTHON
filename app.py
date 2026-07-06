import csv
def save_expenses_to_csv(expenses, filename):
    with open("expenses.csv", mode='w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Name", "Amount", "Category", "Date"])
        for expense in expenses:
            writer.writerow([expense["name"], expense["amount"], expense["category"], expense["date"]])
expenses=[]
def add_expense():
    name=input("enter the name:")
    amount=int(input("enter the amount:"))
    category=input("enter the category:")
    date=input("enter the date:")
    expense={"name":name,"amount":amount,"category":category,"date":date}
    expenses.append(expense)
    save_expenses_to_csv(expenses, "expenses.csv")
    print("expense added successfully!! \n")
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return
    print("YOUR EXPENSES:")
    for expense in expenses:
        print(f"- {expense['name'] }- ${expense['amount']} - ({expense['category']}) - Date: {expense['date']}")
    print()
def delete_expense():
    name = input("Enter the name of the expense to delete: ")
    for expense in expenses:
        if expense["name"] == name:
            expenses.remove(expense)
            with open("expenses.csv", mode='w', newline='') as file:
                writer=csv.writer(file)
                writer.writerow(["Name", "Amount", "Category","Date"])
                for expense in expenses:
                    writer.writerow([expense["name"], expense["amount"], expense["category"], expense["date"]])
            print(f"Expense '{name}' deleted successfully!\n")
            return
    print(f"No expense found with the name '{name}'.\n")
def show_category_total(expenses):
    category_total={}
    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]
        if category in category_total:
            category_total[category]+=amount
        else:
            category_total[category]=amount
    print("category wise total spending:")
    for category,total in category_total.items():
        print(f"{category}: ${total}")
def show_overall_total(expenses):
    total=0
    for expense in expenses:
        total+=expense["amount"]
    print(f"Overall total spending: ${total}")
def load_expenses_from_csv():
    try:
        with open("expenses.csv", mode='r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                expense={"name":row["Name"],"amount":int(row["Amount"]),"category":row["Category"],"date":row["Date"]}
                expenses.append(expense)
    except FileNotFoundError:
        pass
def search_by_category():
    found=False
    category=input("Enter the category to search for: ")
    for expense in expenses:
        if expense["category"] == category:
            print(f"- {expense['name'] }- ${expense['amount']} - ({expense['category']}) - Date: {expense['date']}")
            found=True
    if not found:
        print(f"No expenses found in the category '{category}'.")
def search_by_date():
    found=False
    date=input("Enter the date to search for (DD-MM-YYYY): ")
    for expense in expenses:
        if expense["date"] == date:
            print(f"- {expense['name'] }- ${expense['amount']} - ({expense['category']}) - Date: {expense['date']}")
            found=True
    if not found:
        print(f"No expenses found on the date '{date}'.")
def monthly_summary(expenses):
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    total = 0
    category_totals = {}

    for expense in expenses:
        date = expense["date"]

        parts = date.split("-")
        if len(parts) != 3:
            continue   # skip invalid date format

        day, exp_month, exp_year = parts

        if exp_month == month and exp_year == year:
            amount = expense["amount"]
            total += amount

            category = expense["category"]
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    print(f"\nExpense Summary for {month}-{year}")
    print(f"Total Spent: ₹{total}")

    if total == 0:
        print("No expenses found for this month.")
    else:
        print("Category-wise spending:")
        for category, amount in category_totals.items():
            print(f"{category}: ₹{amount}")
def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4. Show category total")
        print("5. Show overall total spending")
        print("6. Search by category")
        print("7. Search by date")
        print("8. Monthly Summary")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_category_total(expenses)
        elif choice == "5":
            show_overall_total(expenses)
        elif choice == "6":
            search_by_category()
        elif choice == "7":
            search_by_date()
        elif choice == "8":
            monthly_summary(expenses)
        elif choice == "9":
            print("Exiting expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
load_expenses_from_csv()
main()
