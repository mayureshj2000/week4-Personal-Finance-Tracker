###Personal Finance Tracker
##Project Description
A comprehensive personal finance tracking application that helps users manage their expenses, categorize spending, and generate insightful reports. Data is persisted to JSON with backups and can be exported to CSV for external analysis.

#Features
Add expenses with full input validation (date, amount, category, description)
View all expenses in a clean tabular text format
Search expenses by keyword or category
Categorize expenses (Food, Transport, Entertainment, Bills, Shopping, Other)
Save data to JSON file with automatic timestamped backups
Load data on startup with graceful error handling and recovery
Generate monthly expense reports (total + per-category breakdown)
View category-wise spending breakdown with percentages
Set and track monthly budgets per category (stored in budgets.json)
Export data to CSV for external tools (Excel, Sheets, etc.)
User-friendly text menu interface

#How to Run
From project root
cd week4-finance-tracker

#Option 1: via run.py
python run.py

#Option 2: direct main
python main.py
