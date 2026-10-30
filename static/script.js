
const expenseForm = document.getElementById("expense-form");
const expenseList = document.getElementById("expense-list");


// COMMON API FUNCTION
async function apiRequest(url, method = "GET", data = null) {
    const options = { method, headers: {} };

    if (data !== null) {
        options.headers["Content-Type"] = "application/json";
        options.body = JSON.stringify(data);
    }

    const response = await fetch(url, options);
    const result = await response.json();

    if (!response.ok) {
        throw new Error(result.error || "Something went wrong");
    }

    return result;
}


// DISPLAY RESULTS IN A TABLE
function createTable(expenses) {
    if (!expenses.length) {
        return "<p>No expenses found.</p>";
    }

    let html = `
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Amount</th>
                    <th>Category</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody>
    `;

    expenses.forEach(expense => {
        html += `
            <tr>
                <td>${escapeHTML(expense.name)}</td>
                <td>₹${Number(expense.amount).toFixed(2)}</td>
                <td>${escapeHTML(expense.category)}</td>
                <td>${escapeHTML(expense.date)}</td>
            </tr>
        `;
    });

    return html + "</tbody></table>";
}


// SAFELY DISPLAY USER-ENTERED TEXT
function escapeHTML(value) {
    return String(value).replace(/[&<>"']/g, character => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    })[character]);
}


// LOAD ALL EXPENSES
async function loadExpenses() {
    try {
        const expenses = await apiRequest("/api/expenses");

        displayExpenses(expenses);
        updateSummary(expenses);

    } catch (error) {
        expenseList.innerHTML =
            `<tr><td colspan="5">${escapeHTML(error.message)}</td></tr>`;
    }
}


// DISPLAY TRANSACTIONS WITH DELETE BUTTONS
function displayExpenses(expenses) {
    expenseList.innerHTML = "";

    if (!expenses.length) {
        expenseList.innerHTML =
            '<tr><td colspan="5">No expenses found.</td></tr>';
        return;
    }

    expenses.forEach(expense => {
        const row = document.createElement("tr");

        const values = [
            expense.name,
            `₹${Number(expense.amount).toFixed(2)}`,
            expense.category,
            expense.date
        ];

        values.forEach(value => {
            const cell = document.createElement("td");
            cell.textContent = value;
            row.appendChild(cell);
        });

        const actionCell = document.createElement("td");
        const deleteButton = document.createElement("button");

        deleteButton.textContent = "Delete";
        deleteButton.style.background = "#dc3545";

        deleteButton.addEventListener("click", async () => {
            if (!confirm(`Delete ${expense.name} dated ${expense.date}?`)) {
                return;
            }

            try {
                await apiRequest("/api/expenses/delete", "POST", {
                    name: expense.name,
                    date: expense.date
                });

                alert("Expense deleted successfully!");
                loadExpenses();

            } catch (error) {
                alert(error.message);
            }
        });

        actionCell.appendChild(deleteButton);
        row.appendChild(actionCell);
        expenseList.appendChild(row);
    });
}


// UPDATE DASHBOARD CARDS
function updateSummary(expenses) {
    const total = expenses.reduce(
        (sum, expense) => sum + Number(expense.amount), 0
    );

    const now = new Date();
    const month = String(now.getMonth() + 1).padStart(2, "0");
    const year = String(now.getFullYear());

    const monthlyTotal = expenses.reduce((sum, expense) => {
        const parts = expense.date.split("-");
        if (parts[1] === month && parts[2] === year) {
            return sum + Number(expense.amount);
        }
        return sum;
    }, 0);

    document.getElementById("total-expenses").textContent =
        `₹${total.toFixed(2)}`;

    document.getElementById("monthly-expenses").textContent =
        `₹${monthlyTotal.toFixed(2)}`;

    document.getElementById("transaction-count").textContent =
        expenses.length;
}


// ADD EXPENSE
expenseForm.addEventListener("submit", async event => {
    event.preventDefault();

    const expense = {
        name: document.getElementById("name").value.trim(),
        amount: document.getElementById("amount").value,
        category: document.getElementById("category").value.trim(),
        date: document.getElementById("date").value
    };

    try {
        const result = await apiRequest("/api/expenses", "POST", expense);

        document.getElementById("form-message").textContent = result.message;
        expenseForm.reset();
        loadExpenses();

    } catch (error) {
        document.getElementById("form-message").textContent = error.message;
    }
});


// EDIT EXPENSE
document.getElementById("edit-form").addEventListener("submit", async event => {
    event.preventDefault();

    const data = {
        old_name: document.getElementById("edit-name").value.trim(),
        old_date: document.getElementById("edit-date").value,
        name: document.getElementById("new-name").value.trim(),
        amount: document.getElementById("new-amount").value,
        category: document.getElementById("new-category").value.trim(),
        date: document.getElementById("new-date").value
    };

    try {
        const result = await apiRequest("/api/expenses/edit", "POST", data);

        document.getElementById("edit-message").textContent = result.message;
        event.target.reset();
        loadExpenses();

    } catch (error) {
        document.getElementById("edit-message").textContent = error.message;
    }
});


// SEARCH BY CATEGORY
document.getElementById("category-search-form").addEventListener("submit", async event => {
    event.preventDefault();

    const category = document.getElementById("search-category-input").value;

    try {
        const result = await apiRequest(
            `/api/search/category?category=${encodeURIComponent(category)}`
        );

        document.getElementById("category-search-results").innerHTML =
            createTable(result);

    } catch (error) {
        document.getElementById("category-search-results").textContent =
            error.message;
    }
});


// SEARCH BY DATE
document.getElementById("date-search-form").addEventListener("submit", async event => {
    event.preventDefault();

    const date = document.getElementById("search-date-input").value;

    try {
        const result = await apiRequest(
            `/api/search/date?date=${encodeURIComponent(date)}`
        );

        document.getElementById("date-search-results").innerHTML =
            createTable(result);

    } catch (error) {
        document.getElementById("date-search-results").textContent =
            error.message;
    }
});


// CATEGORY-WISE TOTAL
document.getElementById("category-total-button").addEventListener("click", async () => {
    try {
        const result = await apiRequest("/api/category-totals");

        let html = "<ul>";

        for (const [category, amount] of Object.entries(result)) {
            html += `<li>${escapeHTML(category)}: ₹${Number(amount).toFixed(2)}</li>`;
        }

        document.getElementById("category-total-results").innerHTML =
            html + "</ul>";

    } catch (error) {
        alert(error.message);
    }
});


// OVERALL TOTAL
document.getElementById("overall-total-button").addEventListener("click", async () => {
    try {
        const result = await apiRequest("/api/overall-total");

        document.getElementById("overall-total-result").textContent =
            `Total Spending: ₹${Number(result.total).toFixed(2)}`;

    } catch (error) {
        alert(error.message);
    }
});


// MONTHLY SUMMARY
document.getElementById("monthly-summary-button").addEventListener("click", async () => {
    try {
        const result = await apiRequest("/api/monthly-summary");

        let html = "<ul>";

        for (const [month, amount] of Object.entries(result)) {
            html += `<li>${escapeHTML(month)}: ₹${Number(amount).toFixed(2)}</li>`;
        }

        document.getElementById("monthly-summary-results").innerHTML =
            html + "</ul>";

    } catch (error) {
        alert(error.message);
    }
});


// HIGHEST SPENDING CATEGORY
document.getElementById("highest-category-button").addEventListener("click", async () => {
    try {
        const result = await apiRequest("/api/highest-category");

        document.getElementById("highest-category-result").textContent =
            result.category
                ? `${result.category}: ₹${Number(result.amount).toFixed(2)}`
                : "No expenses found.";

    } catch (error) {
        alert(error.message);
    }
});


// PREDICT NEXT MONTH
document.getElementById("predict-button").addEventListener("click", async () => {
    const resultElement = document.getElementById("prediction-result");
    resultElement.textContent = "Calculating prediction...";

    try {
        const result = await apiRequest("/api/predict", "POST");

        resultElement.textContent =
            `Estimated next month's expenses: ₹${Number(result.prediction).toFixed(2)}`;

    } catch (error) {
        resultElement.textContent = error.message;
    }
});


// INITIAL LOAD
loadExpenses();
