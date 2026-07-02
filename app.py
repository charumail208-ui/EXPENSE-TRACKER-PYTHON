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
def show_total_spending():
    total=0
    for expense in expenses:
        total+=expense["amount"]
    return total

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spending")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Total Spending: $", show_total_spending())
        elif choice == "4":
            print("Exiting expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()
