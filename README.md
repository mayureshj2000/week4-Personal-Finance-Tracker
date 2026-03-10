###Personal Finance Tracker

##Project Description
A comprehensive personal finance tracking application that helps users manage their expenses, categorize spending, and generate insightful reports. Data is persisted to JSON with backups and can be exported to CSV for external analysis.

#Features
1. Add expenses with full input validation (date, amount, category, description)
2. View all expenses in a clean tabular text format
3. Search expenses by keyword or category
4. Categorize expenses (Food, Transport, Entertainment, Bills, Shopping, Other)
5. Save data to JSON file with automatic timestamped backups
6. Load data on startup with graceful error handling and recovery
7. Generate monthly expense reports (total + per-category breakdown)
8. View category-wise spending breakdown with percentages
9. Set and track monthly budgets per category (stored in budgets.json)
10. Export data to CSV for external tools (Excel, Sheets, etc.)
11. User-friendly text menu interface

#How to Run
From project root

cd week4-finance-tracker

#Option 1: via run.py
python run.py

#Option 2: direct main
python main.py


##OUTPUT:

python run.py 
Current dir: /workspaces/week4-Personal-Finance-Tracker
Files: ['.git', 'run.py', 'expense.py', 'main.py', 'file_handler.py', 'reports.py', 'README.md', 'expense_manager.py']
expense.py exists? True
1Loaded 0 expenses.
============================================================
          PERSONAL FINANCE TRACKER
============================================================

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9):1

--- ADD EXPENSE ---
Categories: Food, Transport, Entertainment, Utilities, Shopping, Other
Amount: 500
Category: Food
Description: Pizza
Data saved successfully.

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 1

--- ADD EXPENSE ---
Categories: Food, Transport, Entertainment, Utilities, Shopping, Other
Amount: 300          
Category: Transport
Description: Cab
Data saved successfully.

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 1

--- ADD EXPENSE ---
Categories: Food, Transport, Entertainment, Utilities, Shopping, Other
Amount: 700          
Category: Entertainment
Description: Movie
Data saved successfully.

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 1

--- ADD EXPENSE ---
Categories: Food, Transport, Entertainment, Utilities, Shopping, Other
Amount: 2000
Category: Shopping
Description: Clothes
Data saved successfully.

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 2

--- ALL EXPENSES ---
1. 2026-03-10 | Food | Pizza | ₹500.00
2. 2026-03-10 | Transport | Cab | ₹300.00
3. 2026-03-10 | Entertainment | Movie | ₹700.00
4. 2026-03-10 | Shopping | Clothes | ₹2000.00

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 3

--- SEARCH EXPENSES ---
Enter keyword/category: Food
1. 2026-03-10 | Food | Pizza | ₹500.00

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 4

--- MONTHLY REPORT ---
Enter YYYY-MM (e.g. 2026-03): 2026-03
Monthly Report (2026-03): Total $3500.00
Shopping: $2000.00 (57.1%)
Entertainment: $700.00 (20.0%)
Food: $500.00 (14.3%)
Transport: $300.00 (8.6%)


========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 5

--- CATEGORY BREAKDOWN ---
Shopping: ₹2000.00 (57.1%)
Entertainment: ₹700.00 (20.0%)
Food: ₹500.00 (14.3%)
Transport: ₹300.00 (8.6%)

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 6

--- SET/UPDATE BUDGET --- (placeholder)

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 7

--- EXPORT DATA ---
Exported to data/exports/expenses.csv

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 8

--- STATISTICS ---
Total: ₹3500.00, Count: 4, Average: ₹875.00

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 9

--- BACKUP/RESTORE --- (auto via save_expenses backups)

========================================
MAIN MENU
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Monthly Report
5. Category Breakdown
6. Budget
7. Export CSV
8. Stats
9. Backup
0. Exit
========================================

Enter your choice (0-9): 0
Data saved successfully.

Thank you for using Personal Finance Tracker!
