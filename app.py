import csv
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime
def save_expenses_to_csv(expenses, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Amount", "Category", "Date"])

        for expense in expenses:
            writer.writerow([
                expense["name"],
                expense["amount"],
                expense["category"],
                expense["date"]
            ])
expenses=[]
def add_expense():
    name=input("enter the name:")
    try:
        amount = int(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid integer.\n")
        return
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
    if not expenses:
        print("No expenses found.\n")
        return

    name = input("Enter the name of the expense to delete: ").strip()
    date = input("Enter the date of the expense (DD-MM-YYYY): ").strip()

    for expense in expenses:
        if (expense["name"].strip().lower() == name.lower()
                and expense["date"].strip() == date):

            expenses.remove(expense)

            save_expenses_to_csv(expenses, "expenses.csv")

            print(f"Expense '{name}' on {date} deleted successfully!\n")
            return

    print(f"No expense found with the name '{name}' on {date}.\n")
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
        with open("expenses.csv", mode="r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                print("expenses.csv is empty. Starting with no expenses.\n")
                return

            for row in reader:
                try:
                    expense = {
                        "name": row["Name"],
                        "amount": int(row["Amount"]),
                        "category": row["Category"],
                        "date": row["Date"]
                    }
                    expenses.append(expense)

                except (KeyError, ValueError, TypeError):
                    print("Skipping an invalid row:", row)

    except FileNotFoundError:
        pass
def search_by_category():
    if not expenses:
        print("No expenses found.\n")
        return

    category = input("Enter the category to search for: ").strip()

    found = False

    print(f"\nExpenses in category: {category}")
    print("-----------------------------------")

    for expense in expenses:
        if expense["category"].strip().lower() == category.lower():

            print(
                f"Name: {expense['name']} | "
                f"Amount: ₹{expense['amount']} | "
                f"Category: {expense['category']} | "
                f"Date: {expense['date']}"
            )

            found = True

    if not found:
        print(f"No expenses found in the category '{category}'.")

    print()
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
def show_highest_category():
    if not expenses:
        print("No expenses found.\n")
        return

    category_total = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount

    highest_category = max(category_total, key=category_total.get)

    print("\nCategory with Highest Spending:")
    print(f"Category: {highest_category}")
    print(f"Total Spent: ₹{category_total[highest_category]}\n")


def predict_next_month_expense():
    if not expenses:
        print("No expenses available for prediction.\n")
        return

    df = pd.DataFrame(expenses)

    df["date"] = pd.to_datetime(
        df["date"], format="%d-%m-%Y", errors="coerce"
    )

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["date", "amount"])

    if df.empty:
        print("No valid expense records found.\n")
        return

    # Create a month column
    df["month"] = df["date"].dt.to_period("M")

    # Calculate total spending for each month
    monthly_total = df.groupby("month")["amount"].sum().sort_index()

    # Create a continuous range of months
    all_months = pd.period_range(
        start=monthly_total.index.min(),
        end=monthly_total.index.max(),
        freq="M"
    )

    monthly_total = monthly_total.reindex(all_months, fill_value=0)

    if len(monthly_total) < 2:
        print("Prediction requires at least two months of data.\n")
        return

    # Train the overall expense prediction model
    X = pd.DataFrame({
        "month_number": range(len(monthly_total))
    })
    y = monthly_total.values

    overall_model = LinearRegression()
    overall_model.fit(X, y)

    next_month_number = len(monthly_total)
    next_month = monthly_total.index[-1] + 1

    overall_prediction = overall_model.predict(
        pd.DataFrame({"month_number": [next_month_number]})
    )[0]

    overall_prediction = max(0, overall_prediction)

    # Calculate spending by category for each month
    category_monthly = df.pivot_table(
        index="month",
        columns="category",
        values="amount",
        aggfunc="sum",
        fill_value=0
    )

    # Include months with no recorded spending
    category_monthly = category_monthly.reindex(
        all_months, fill_value=0
    )

    # Predict next month's spending for each category
    category_predictions = {}

    for category in category_monthly.columns:
        category_data = category_monthly[category]

        category_model = LinearRegression()
        category_model.fit(X, category_data.values)

        predicted_amount = category_model.predict(
            pd.DataFrame({
                "month_number": [next_month_number]
            })
        )[0]

        category_predictions[category] = max(0, predicted_amount)

    # Display results
    print("\n======= MONTHLY EXPENSE PREDICTION =======")
    print(f"\nHistorical monthly spending:")

    for month, total in monthly_total.items():
        print(f"{month}: ₹{total:.2f}")

    print(f"\nOverall prediction for {next_month}:")
    print(f"Predicted expense: ₹{overall_prediction:.2f}")

    print(f"\n======= CATEGORY-WISE PREDICTION =======")

    for category, amount in sorted(category_predictions.items()):
        print(f"{category}: ₹{amount:.2f}")

    category_total = sum(category_predictions.values())

    print("----------------------------------------")
    print(f"Total of category predictions: ₹{category_total:.2f}")
    print(f"Overall prediction: ₹{overall_prediction:.2f}")
    print("\nModel: Linear Regression")
    print(f"Months analyzed: {len(monthly_total)}")
    print("========================================\n")

def edit_expense():
    if not expenses:
        print("No expenses found.\n")
        return

    name = input("Enter the name of the expense to edit: ")

    for expense in expenses:
        if expense["name"].lower() == name.lower():
            print("Leave blank if you don't want to change a field.")

            new_name = input(f"Enter new name [{expense['name']}]: ")
            new_amount = input(f"Enter new amount [{expense['amount']}]: ")
            new_category = input(f"Enter new category [{expense['category']}]: ")
            new_date = input(f"Enter new date [{expense['date']}]: ")

            if new_name != "":
                expense["name"] = new_name
            if new_amount != "":
                expense["amount"] = int(new_amount)
            if new_category != "":
                expense["category"] = new_category
            if new_date != "":
                expense["date"] = new_date

            save_expenses_to_csv(expenses, "expenses.csv")
            print("Expense updated successfully!\n")
            return

    print(f"No expense found with the name '{name}'.\n")
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
        print("9.Show highest category")
        print("10. Edit Expense")
        print("11. Predict Next Month's Expenses")
        print("12. Exit")
        choice = input("Enter your choice (1-12): ")
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
            show_highest_category()
        elif choice == "10":
            edit_expense()
        elif choice == "11":
            predict_next_month_expense()
        elif choice == "12":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
load_expenses_from_csv()
main()