# EXPENSE AND BUDGET TRACKER
# Member 3 - Budget Analysis

import pandas as pd

# Read expense data
df = pd.read_csv("Expenses.tsv", sep="\t")
# Create Budget Table
budget = {
    "Food": 800,
    "Travel": 500,
    "Education": 1600,
    "Utilities": 600,
    "Shopping": 700,
    "Medical": 300,
    "Entertainment": 300
}

# Calculate actual expenses
actual = df.groupby("Category")["Amount"].sum()

# Create Budget Analysis Table
report = pd.DataFrame({
    "Budget": pd.Series(budget),
    "Actual Expense": actual
})

report = report.fillna(0)

# Calculate remaining budget
report["Remaining Budget"] = (
    report["Budget"] - report["Actual Expense"]
)

# Identify spending status
report["Status"] = report["Remaining Budget"].apply(
    lambda x: "Overspending" if x < 0
    else "Within Budget"
)

# Display Budget Report
print("\n===== BUDGET ANALYSIS REPORT =====")

print(report)

# Calculate totals
print("\nTotal Budget:", report["Budget"].sum())

print("Total Expenses:", report["Actual Expense"].sum())

print("Remaining Budget:", report["Remaining Budget"].sum())

print("\nBudget Analysis Completed Successfully!")
# Save Budget Report
report.index.name = "Category"
report.to_csv("Budget_Report.csv")

print("Budget Report saved successfully!")
import matplotlib.pyplot as plt

# Create Budget Comparison Chart
report[["Budget", "Actual Expense"]].plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Budget vs Actual Expenses")
plt.xlabel("Expense Category")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("Budget_Comparison_Chart.png")

plt.show()