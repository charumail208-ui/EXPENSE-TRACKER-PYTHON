import csv
def save_expenses_to_csv(expenses, filename):
    with open("expenses.csv", mode='w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Name", "Amount", "Category"])
        for expense in expenses:
            writer.writerow([expense["name"], expense["amount"], expense["category"]])
expenses=[]
def add_expense():
    name=input("enter the name:")
    amount=int(input("enter the amount:"))
    category=input("enter the category:")
    expense={"name":name,"amount":amount,"category":category}
    expenses.append(expense)
    save_expenses_to_csv(expenses, "expenses.csv")
    print("expense added successfully!! \n")
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return
    print("YOUR EXPENSES:")
    for expense in expenses:
        print(f"- {expense['name'] }- ${expense['amount']} - ({expense['category']})")
    print()
def delete_expense():
    name = input("Enter the name of the expense to delete: ")
    for expense in expenses:
        if expense["name"] == name:
            expenses.remove(expense)
            with open("expenses.csv", mode='w', newline='') as file:
                writer=csv.writer(file)
                writer.writerow(["Name", "Amount", "Category"])
                for expense in expenses:
                    writer.writerow([expense["name"], expense["amount"], expense["category"]])
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
                expense={"name":row["Name"],"amount":int(row["Amount"]),"category":row["Category"]}
                expenses.append(expense)
    except FileNotFoundError:
        pass
def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4. Show category total")
        print("5. Show overall total spending")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
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
            print("Exiting expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
load_expenses_from_csv()
main()
