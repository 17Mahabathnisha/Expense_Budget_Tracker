# EXPENSE AND BUDGET TRACKER
# Member 2 - Expense Categorization

import pandas as pd
import os

# Read Member 1 Excel data
file_path = os.path.join(
    os.path.dirname(__file__),
    "Expenses.xlsx"
)

df = pd.read_excel(file_path)

# Convert column names into lowercase
df.columns = df.columns.str.strip().str.lower()

# Convert Excel data into dictionary
expenses = df.to_dict("records")

# Keyword-based category rules
category_rules = {
    "Food": ["breakfast", "lunch", "dinner", "hotel", "grocery", "food", "snacks", "vegetables"],
    "Travel": ["bus", "train", "petrol", "taxi", "auto"],
    "Shopping": ["shopping", "clothes", "shoes"],
    "Entertainment": ["movie", "game", "cinema"],
    "Education": ["notebook", "books", "pen", "stationery", "fees"],
    "Utilities": ["recharge", "internet", "mobile"],
    "Medical": ["medicine", "hospital", "doctor"]
}

# Function to categorize expenses
def categorize_expense(description):
    description = str(description).lower()

    for category, keywords in category_rules.items():
        for keyword in keywords:
            if keyword in description:
                return category

    return "Others"

# Apply categories
for expense in expenses:
    expense["category"] = categorize_expense(
        expense["description"]
    )

# Display categorized expenses
print("\n----- EXPENSE REGISTER -----")

for expense in expenses:
    print(expense)

# Generate category summary
category_summary = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category not in category_summary:
        category_summary[category] = 0

    category_summary[category] += amount

# Display category summary
print("\n----- CATEGORY SUMMARY -----")

for category, total in category_summary.items():
    print(category, ":", total)
    # Calculate total expenses
total_expenses = sum(category_summary.values())

print("\nTotal Expenses:", total_expenses)

print("\nCategorization Completed Successfully!")