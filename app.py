expenses=[]
def add_expense():
    name=input("enter your name:")
    amount=int(input("enter your amount:"))
    category=input("enter your category:")
    expense={"name":name,"amount":amount,"category":category}
    expenses.append(expense)
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
def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4. Show category total")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_category_total(expenses)
        elif choice == "5":
            print("Exiting expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()
