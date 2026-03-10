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
