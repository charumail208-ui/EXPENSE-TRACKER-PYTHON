# Expense Tracker with Monthly Expense Prediction

A Python-based **Expense Tracker and Data Analysis System** developed as part of the **Introduction to Data Science (IDS) project**.

This project helps users record, manage, track, and analyze their daily expenses through a menu-driven console application. It uses CSV file handling for persistent data storage and applies **Machine Learning techniques using Linear Regression** to predict future monthly expenses based on historical spending patterns.

The project combines Python programming, data processing, exploratory analysis, and predictive analytics to transform everyday expense records into meaningful financial insights.

---

## Features

### 1. Expense Management
- Add new expenses with name, amount, category, and date.
- View all recorded expenses.
- Edit existing expense details.
- Delete expenses and automatically update the CSV file.
- Automatically load previously saved expenses when the program starts.

### 2. Expense Analysis
- Calculate category-wise total spending.
- Calculate overall total expenditure.
- Search expenses by category.
- Search expenses by date.
- Generate monthly expense summaries.
- Display category-wise spending for a selected month.
- Identify the category with the highest total spending.

### 3. Machine Learning-Based Expense Prediction
- Predict the next month's overall expenditure.
- Generate category-wise expense predictions.
- Analyze historical monthly spending patterns.
- Use **Linear Regression** to estimate future expenses.
- Handle months with no recorded expenses by including them as zero-spending months.

---

## Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CSV | Expense data storage |
| Pandas | Data processing and analysis |
| NumPy | Numerical computing |
| Scikit-learn | Machine Learning |
| Linear Regression | Predicting future monthly expenses |

---

## Machine Learning Algorithm

### Linear Regression

The project uses **Linear Regression**, a supervised Machine Learning algorithm, to predict future expenditure.

The prediction process involves:

1. Reading historical expense records from the CSV file.
2. Converting expense dates into monthly periods.
3. Calculating the total expenditure for each month.
4. Creating a continuous monthly dataset.
5. Training a Linear Regression model using monthly spending trends.
6. Predicting the expenditure for the next month.
7. Applying separate Linear Regression models to estimate category-wise spending.

The system provides:
- Overall monthly expense prediction.
- Category-wise monthly expense prediction.

**Note:** Predictions are estimates based on historical spending patterns and are not guaranteed future expenses. The model requires at least two months of valid data.

---

## How the Project Works

The application provides a menu-driven interface with the following options:

1. **Add Expense** – Record a new expense.
2. **View Expenses** – Display all recorded expenses.
3. **Delete Expense** – Remove an existing expense.
4. **Show Category Total** – Calculate category-wise spending.
5. **Show Overall Total Spending** – Calculate total expenditure.
6. **Search by Category** – Find expenses belonging to a particular category.
7. **Search by Date** – Retrieve expenses recorded on a specific date.
8. **Monthly Summary** – Generate a monthly expenditure report with category-wise totals.
9. **Show Highest Spending Category** – Identify the category with the highest expenditure.
10. **Edit Expense** – Modify existing expense details.
11. **Predict Next Month's Expenses** – Estimate overall and category-wise future expenditure using Linear Regression.
12. **Exit** – Close the application.

---

## Data Storage

All expense records are stored in a CSV file named `expenses.csv`.

Each record contains:
- Name
- Amount
- Category
- Date

### Sample CSV Format

```csv
Name,Amount,Category,Date
Groceries,2500,Food,05-01-2026
Vegetables,1200,Food,12-01-2026
Bus Pass,800,Travel,15-01-2026
Electricity Bill,1500,Utilities,20-01-2026
Movie,500,Entertainment,25-01-2026
```

The program automatically reads saved records when it starts and updates the CSV file whenever expenses are added, edited, or deleted.

---

## Installation and Execution

### Prerequisites
- Python 3.x
- VS Code or any Python-supported IDE

### Step 1: Clone the Repository

```bash
git clone https://github.com/charumail208-ui/EXPENSE-TRACKER-PYTHON.git
```

### Step 2: Navigate to the Project Folder

```bash
cd EXPENSE-TRACKER-PYTHON
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy scikit-learn
```

### Step 4: Run the Application

```bash
python app.py
```

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Python functions, lists, and dictionaries.
- File handling and CSV operations.
- Data cleaning and preprocessing.
- Data manipulation using Pandas.
- Numerical computing using NumPy.
- Exploratory data analysis and expense summarization.
- Supervised Machine Learning concepts.
- Implementing Linear Regression.
- Training models using historical data.
- Predictive analytics and interpreting results.
- Git and GitHub for project version control.

---

## Future Enhancements

- Develop a web-based interface using HTML, CSS, JavaScript, and Flask.
- Add interactive charts and visualizations.
- Implement user authentication.
- Introduce budget management and spending alerts.
- Improve prediction accuracy using larger historical datasets.
- Add downloadable monthly expense reports.

---

## Author

**Charutha Rajeevan**

AI & Data Science Engineering Student

**GitHub Repository:**  
https://github.com/charumail208-ui/EXPENSE-TRACKER-PYTHON