EXPENSE AND BUDGET TRACKER

Member 2 – Expense Categorization Procedure

1. Introduction

The Expense Categorization module is used to automatically classify expenses into different categories based on the description of each transaction.

It reduces manual work and helps users understand where their money is spent.

2. Objective

- To read expense data from an Excel file.
- To identify expense categories using keywords.
- To classify expenses automatically.
- To calculate category-wise expense totals.
- To calculate the total expenses.

3. Technologies Used

- Python
- Pandas
- OS module
- Microsoft Excel
- Visual Studio Code

4. Input Dataset

The module reads the Excel file named "expenses.xlsx".

The required columns are:

| Column | Description |
|---|---|
| Date | Date of transaction |
| Description | Details of the expense |
| Amount | Expense amount |

The column names are converted into lowercase, and extra spaces are removed.

5. Expense Categories and Business Rules

| Category | Keywords |
|---|---|
| Food | Breakfast, Lunch, Dinner, Hotel, Grocery, Food, Snacks, Vegetables |
| Travel | Bus, Train, Petrol, Taxi, Auto |
| Shopping | Shopping, Clothes, Shoes |
| Entertainment | Movie, Game, Cinema |
| Education | Notebook, Books, Pen, Stationery, Fees |
| Utilities | Recharge, Internet, Mobile |
| Medical | Medicine, Hospital, Doctor |
| Others | Descriptions that do not match any keyword |

6. Working Procedure

Step 1: Import Libraries

The Pandas and OS libraries are imported.

Step 2: Read Excel File

The program reads the expense data from the Excel file using "pd.read_excel()".

Step 3: Process Column Names

All column names are converted into lowercase, and extra spaces are removed.

Step 4: Convert Data into Dictionary

The Excel records are converted into a list of dictionaries.

Step 5: Apply Categorization Rules

The program checks each expense description against predefined keywords.

The matching category is assigned to the expense.

If no keyword matches, the expense is classified as Others.

Step 6: Display Expense Register

The program displays all expense records with their assigned categories.

Step 7: Generate Category Summary

The program calculates the total amount spent in each category.

Step 8: Calculate Total Expenses

The program adds all category totals and displays the overall expense amount.

7. Output

The program generates:

1. Expense Register with assigned categories.
2. Category-wise expense summary.
3. Total expense amount.
4. Successful completion message.

8. Testing Details

The following sample descriptions can be used to verify the categorization rules.

Test Input| Expected Category
Breakfast| Food
Bus ticket| Travel
Shopping for clothes| Shopping
Movie ticket| Entertainment
Notebook purchase| Education
Mobile recharge| Utilities
Medicine purchase| Medical
Other miscellaneous expense| Others

The actual results must be compared with the expected categories after executing the program.

9. Limitations

- Categorization depends on predefined keywords.
- New keywords must be added manually.
- Descriptions without matching keywords are classified as Others.
- The program requires the correct Excel file and column names.

10. Conclusion

The Expense Categorization module automatically classifies expenses using Python and keyword-based rules.

It also generates category-wise summaries and calculates total expenses.

This module helps users understand their spending patterns and supports the overall Expense and Budget Tracker project.

## 7. Testing Details

| Test Case | Expected Result | Status |
|---|---|---|
| Read Excel file | Expense data should load successfully | Passed |
| Food keyword detection | Should identify Food category | Passed |
| Travel keyword detection | Should identify Travel category | Passed |
| Shopping keyword detection | Should identify Shopping category | Passed |
| Category summary | Should calculate category-wise totals | Passed |
| Total expenses | Should calculate total expense amount | Passed |

## 8. Test Result

The program executed successfully and categorized the sample expenses based on predefined keywords.

- Total Expenses: 3603
- Categorization Status: Completed Successfully