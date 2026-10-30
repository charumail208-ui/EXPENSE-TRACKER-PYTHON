
from flask import Flask, render_template, request, jsonify
import csv
import os
from datetime import datetime
from collections import defaultdict
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "expenses.csv")


# DATE CONVERSION
def parse_date(value):
    for fmt in ("%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(value.strip(), fmt)
        except ValueError:
            continue
    raise ValueError("Invalid date format.")


# LOAD EXPENSES
def load_expenses():
    expenses = []

    if not os.path.exists(CSV_FILE):
        return expenses

    with open(CSV_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        required = {"Name", "Amount", "Category", "Date"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain Name, Amount, Category and Date columns.")

        for row in reader:
            expenses.append({
                "name": row["Name"],
                "amount": float(row["Amount"]),
                "category": row["Category"],
                "date": parse_date(row["Date"]).strftime("%d-%m-%Y")
            })

    return expenses


# SAVE EXPENSES
def save_expenses(expenses):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Name", "Amount", "Category", "Date"]
        )

        writer.writeheader()

        for expense in expenses:
            writer.writerow({
                "Name": expense["name"],
                "Amount": expense["amount"],
                "Category": expense["category"],
                "Date": expense["date"]
            })


# WEBSITE HOME
@app.route("/")
def home():
    return render_template("index.html")


# VIEW ALL EXPENSES
@app.route("/api/expenses", methods=["GET"])
def get_expenses():
    try:
        return jsonify(load_expenses())
    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400


# ADD EXPENSE
@app.route("/api/expenses", methods=["POST"])
def add_expense():
    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    category = str(data.get("category", "")).strip()

    try:
        amount = float(data.get("amount", 0))
        date = parse_date(str(data.get("date", "")))
    except (ValueError, TypeError):
        return jsonify({"error": "Enter a valid amount and date."}), 400

    if not name or not category or amount <= 0:
        return jsonify({"error": "All fields are required and amount must be positive."}), 400

    try:
        expenses = load_expenses()
        expenses.append({
            "name": name,
            "amount": amount,
            "category": category,
            "date": date.strftime("%d-%m-%Y")
        })
        save_expenses(expenses)
    except (ValueError, KeyError, OSError) as error:
        return jsonify({"error": str(error)}), 400

    return jsonify({"message": "Expense added successfully!"}), 201


# DELETE EXPENSE
@app.route("/api/expenses/delete", methods=["POST"])
def delete_expense():
    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()

    try:
        date = parse_date(str(data.get("date", ""))).strftime("%d-%m-%Y")
        expenses = load_expenses()
    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400

    for index, expense in enumerate(expenses):
        if (expense["name"].strip().lower() == name.lower()
                and expense["date"] == date):
            expenses.pop(index)
            save_expenses(expenses)
            return jsonify({"message": "Expense deleted successfully!"})

    return jsonify({"error": "Expense not found."}), 404


# EDIT EXPENSE
@app.route("/api/expenses/edit", methods=["POST"])
def edit_expense():
    data = request.get_json(silent=True) or {}

    old_name = str(data.get("old_name", "")).strip()

    try:
        old_date = parse_date(str(data.get("old_date", ""))).strftime("%d-%m-%Y")
        new_date = parse_date(str(data.get("date", ""))).strftime("%d-%m-%Y")
        new_amount = float(data.get("amount", 0))
    except (ValueError, TypeError):
        return jsonify({"error": "Enter valid dates and amount."}), 400

    new_name = str(data.get("name", "")).strip()
    new_category = str(data.get("category", "")).strip()

    if not old_name or not new_name or not new_category or new_amount <= 0:
        return jsonify({"error": "Please fill all fields correctly."}), 400

    try:
        expenses = load_expenses()
    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400

    for expense in expenses:
        if (expense["name"].strip().lower() == old_name.lower()
                and expense["date"] == old_date):
            expense.update({
                "name": new_name,
                "amount": new_amount,
                "category": new_category,
                "date": new_date
            })
            save_expenses(expenses)
            return jsonify({"message": "Expense updated successfully!"})

    return jsonify({"error": "Original expense not found."}), 404


# SEARCH BY CATEGORY
@app.route("/api/search/category", methods=["GET"])
def search_category():
    category = request.args.get("category", "").strip()

    try:
        expenses = load_expenses()
    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400

    result = [
        expense for expense in expenses
        if expense["category"].strip().lower() == category.lower()
    ]

    return jsonify(result)


# SEARCH BY DATE
@app.route("/api/search/date", methods=["GET"])
def search_date():
    try:
        date = parse_date(request.args.get("date", "")).strftime("%d-%m-%Y")
        expenses = load_expenses()
    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400

    result = [
        expense for expense in expenses
        if expense["date"] == date
    ]

    return jsonify(result)


# CATEGORY-WISE TOTALS
@app.route("/api/category-totals", methods=["GET"])
def category_totals():
    try:
        expenses = load_expenses()
    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400

    totals = defaultdict(float)

    for expense in expenses:
        totals[expense["category"]] += expense["amount"]

    return jsonify(dict(totals))


# OVERALL TOTAL
@app.route("/api/overall-total", methods=["GET"])
def overall_total():
    try:
        expenses = load_expenses()
    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400

    total = sum(expense["amount"] for expense in expenses)

    return jsonify({"total": round(total, 2)})


# MONTHLY SUMMARY
@app.route("/api/monthly-summary", methods=["GET"])
def monthly_summary():
    try:
        expenses = load_expenses()
    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400

    totals = defaultdict(float)

    for expense in expenses:
        date = parse_date(expense["date"])
        month = date.strftime("%B %Y")
        totals[month] += expense["amount"]

    return jsonify(dict(totals))


# HIGHEST SPENDING CATEGORY
@app.route("/api/highest-category", methods=["GET"])
def highest_category():
    try:
        expenses = load_expenses()
    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400

    totals = defaultdict(float)

    for expense in expenses:
        totals[expense["category"]] += expense["amount"]

    if not totals:
        return jsonify({"category": None, "amount": 0})

    category = max(totals, key=totals.get)

    return jsonify({
        "category": category,
        "amount": round(totals[category], 2)
    })


# NEXT MONTH PREDICTION USING LINEAR REGRESSION
@app.route("/api/predict", methods=["POST"])
def predict_expense():
    try:
        expenses = load_expenses()
    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400

    if not expenses:
        return jsonify({"error": "No expenses available for prediction."}), 400

    monthly_totals = defaultdict(float)

    for expense in expenses:
        date = parse_date(expense["date"])
        key = date.year * 12 + date.month
        monthly_totals[key] += expense["amount"]

    if len(monthly_totals) < 2:
        return jsonify({
            "error": "At least two months of expenses are required."
        }), 400

    first_month = min(monthly_totals)
    last_month = max(monthly_totals)

    months = list(range(first_month, last_month + 1))
    totals = [monthly_totals.get(month, 0) for month in months]

    X = [[i] for i in range(len(months))]

    model = LinearRegression()
    model.fit(X, totals)

    prediction = model.predict([[len(months)]])[0]
    prediction = max(0, float(prediction))

    return jsonify({"prediction": round(prediction, 2)})


if __name__ == "__main__":
    app.run(debug=True)
