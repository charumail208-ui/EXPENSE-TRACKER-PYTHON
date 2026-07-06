# Expense Tracker (Python)

A simple **Python console-based Expense Tracker** built as part of my **90 Days of Coding** challenge and my learning journey in **AI and Data Science**.

This project helps users record, manage, and analyze expenses using a menu-driven interface. Expense data is stored in a **CSV file**, so it remains saved even after closing the program.

---

## Features

* Add a new expense with **name, amount, category, and date**
* View all recorded expenses
* Delete an expense
* Show **category-wise total spending**
* Show **overall total spending**
* Search expenses by **category**
* Search expenses by **date**
* Show **monthly expense summary**
* Save expenses permanently in a **CSV file**
* Load saved expenses automatically when the program starts
* CSV file includes headings for better organization

---

## Technologies Used

* **Python**
* Built-in **CSV module**

---

## How It Works

The program provides a menu-driven console interface with the following options:

1. **Add Expense**
   Add a new expense by entering the expense name, amount, category, and date.

2. **View Expenses**
   Display all saved expenses.

3. **Delete Expense**
   Remove an expense and update the CSV file.

4. **Show Category Total**
   Display the total spending for each category.

5. **Show Overall Total**
   Display the total of all expenses.

6. **Search by Category**
   Show expenses belonging to a specific category.

7. **Search by Date**
   Show expenses recorded on a specific date.

8. **Monthly Summary**
   Display the total spending for a selected month and year, along with category-wise totals for that month.

9. **Exit**
   Close the program safely.

---

## Data Storage

Each expense is stored with:

* **Name**
* **Amount**
* **Category**
* **Date**

Expenses are stored in a CSV file named **`expenses.csv`**.

### Example CSV format:

```csv
Name,Amount,Category,Date
Lunch,120,Food,05-07-2026
Bus,30,Travel,06-07-2026
Book,250,Study,06-07-2026
```

---

## Progress

### Day 1

* Built the basic expense tracker
* Added the ability to store expenses in a list

### Day 2

* Added **category-wise total spending**

### Day 3

* Added **CSV file storage**
* Added **loading expenses from CSV**
* Added **delete expense with CSV update**
* Added **overall total spending**
* Added **CSV headings**

### Day 4

* Added **date** for each expense
* Added **search by category**
* Added **search by date**

### Day 5

* Added **monthly expense summary**
* Displays **total spending for a selected month**
* Displays **category-wise monthly spending**
* Improved understanding of **function creation and data filtering**

---

## Learning Outcomes

Through this project, I practiced:

* Python functions
* Lists and dictionaries
* File handling
* CSV reading and writing
* Menu-driven program design
* Searching and filtering data
* Updating file data after deletion
* Summarizing data month-wise

---

## Future Improvements

* Show **highest spending category**
* Add **budget warning**
* Add **edit expense**
* Create graphs/charts for expense analysis
* Build a **Flask website version**
* Upgrade storage from CSV to a database like **SQLite**

---

## Author

**Charutha Rajeevan**
