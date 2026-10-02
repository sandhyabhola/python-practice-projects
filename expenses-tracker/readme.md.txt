# 💰 Expense Tracker (Console App)

A console-based expense tracker written in Python. You can add, view, search, update and delete expenses, and see reports such as a dashboard summary, monthly report and category-wise spending. All data is saved in a JSON file, so it is still there the next time you run the program.

This is a **practice project** built while learning Python. It was my first project that combines a class, file handling and a third-party library.

---

## Features

- Add an expense (date, category, amount, description)
- View all expenses in a table
- Search expenses by amount, date or keyword
- Update any field of an expense
- Delete an expense
- Reports:
  - Dashboard summary (count, total, average, highest, lowest)
  - Highest expense(s)
  - Lowest expense(s)
  - Monthly report with monthly totals
  - Category-wise spending with grand total
- Input validation for every field
- Data saved automatically in `expenses.json`
- Unique auto-incrementing ID for every expense

---

## Menu Overview

```
============================== EXPENSE TRACKER ==============================
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Update Expense
5. Delete Expense
6. Reports
7. Exit
```

```
============================== REPORT ==============================
1. Dashboard Summary
2. Highest Expense
3. Lowest Expense
4. Monthly Report
5. Category-wise Spending
6. Back
```

---

## Input Rules

| Field       | Rule                                                      |
|-------------|-----------------------------------------------------------|
| Date        | Must be a real date in `YYYY-MM-DD` format                |
| Category    | Letters only, at least 3 characters                       |
| Amount      | Whole number greater than 0                               |
| Description | At least 6 characters and must contain letters            |

---

## How Search Works

- If you type a **number**, it matches expenses with that exact amount.
- If you type a **date** (`YYYY-MM-DD`), it matches expenses on that date.
- Otherwise it looks for the text (not case sensitive) in the category or description.

Update and Delete use the same search. You search first, then choose the expense by its ID from the results.

---

## Data Storage

Expenses are stored in `expenses.json`:

```json
{
    "last_used_id": 1,
    "expenses": [
        {
            "ID": 1,
            "Date": "2026-06-24",
            "Category": "Food",
            "Amount": 30,
            "Description": "Tea time"
        }
    ]
}
```

`last_used_id` keeps track of the last ID given, so IDs are never reused, even after deleting an expense.

---

## Concepts Practiced

- Classes and objects (`ExpensesManager`)
- Static methods (`@staticmethod`) for validation
- File handling with the `json` module (read and write)
- Working with lists and nested dictionaries
- `datetime` module for date validation and monthly grouping
- Exception handling (`try` / `except`)
- Input validation with loops
- Using a third-party library (`tabulate`) to print tables
- Splitting logic into manager methods and input/display functions

---

## How to Run

Requirements: Python 3.x and the `tabulate` library.

```bash
pip install tabulate
python main.py
```

The program needs an `expenses.json` file in the same folder. If you are starting fresh, create it with this content:

```json
{
    "last_used_id": 0,
    "expenses": []
}
```

---

## Project Structure

```
expense-tracker/
├── main.py          # all program logic
└── expenses.json    # saved expense data
```

### Inside main.py

- `load_expenses()` and `save_expenses()` read and write the JSON file
- `ExpensesManager` class handles validation, add, search, update, delete and report calculations
- Input functions handle menu choices and user input checks
- Display functions print tables and reports
- The main menu loop connects everything

---

## Notes

This is a learning project from my Python practice phase. The code is intentionally simple.
