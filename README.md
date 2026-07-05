# Expense Tracker (Python)

A simple **Python console-based Expense Tracker** built as part of my **90 Days of Coding** challenge and learning journey in **AI and Data Science**.

This project helps users record, manage, and analyze their expenses using a menu-driven interface. It also stores expense data in a **CSV file**, so the data remains saved even after closing the program.

---

## Features

* Add a new expense with **name, amount, and category**
* View all recorded expenses
* Delete an expense
* Show **category-wise total spending**
* Show **overall total spending**
* Save expenses permanently in a **CSV file**
* Load saved expenses automatically when the program starts
* CSV file includes **headings** for better organization

---

## Technologies Used

* **Python**
* Built-in **CSV module**

---

## How It Works

The program provides a menu-driven console interface with the following options:

1. **Add Expense**
   Add a new expense by entering the expense name, amount, and category.

2. **View Expenses**
   Display all saved expenses.

3. **Delete Expense**
   Remove an expense and update the CSV file.

4. **Show Category Total**
   Display the total spending for each category.

5. **Show Overall Total**
   Display the total of all expenses.

6. **Exit**
   Close the program safely.

---

## Data Storage

Each expense is stored with:

* **Name**
* **Amount**
* **Category**

Expenses are stored in a CSV file named **`expenses.csv`**.

### Example CSV format:

```csv
Name,Amount,Category
Lunch,120,Food
Bus,30,Travel
Book,250,Study
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

---

## Learning Outcomes

Through this project, I practiced:

* Python functions
* Lists and dictionaries
* File handling
* CSV reading and writing
* Menu-driven program design
* Updating file data after deletion

---

## Future Improvements

* Add **date** for each expense
* Search expenses by category
* Monthly expense summary
* Budget limit warning
* Graphs or charts for expense analysis
* GUI or web-based version of the project

---

## Author

**Charutha Rajeevan**
