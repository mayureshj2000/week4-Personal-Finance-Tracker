# Week4/main.py - FLAT DIR VERSION
import sys
import os
from datetime import datetime

# Point to Week4/ dir (contains all .py files)
WEEK4_DIR = r"/Workspace/Users/mayureshjadhav28122000@gmail.com/Week4"
sys.path.insert(0, WEEK4_DIR)

# Direct imports (all files in same dir)
from expense import Expense, VALID_CATEGORIES
from expense_manager import ExpenseManager
from file_handler import load_expenses, save_expenses, export_to_csv
from reports import generate_monthly_report, category_breakdown


class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        self._load_data()

    def _load_data(self):
        try:
            self.manager.expenses = load_expenses()
            print(f"Loaded {len(self.manager.expenses)} expenses.")
        except Exception as e:
            print(f"Load error (starting fresh): {e}")
            self.manager.expenses = []

    def _save_data(self):
        try:
            save_expenses(self.manager.expenses)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Save error: {e}")

    def run(self):
        print("=" * 60)
        print("          PERSONAL FINANCE TRACKER")
        print("=" * 60)

        while True:
            self._print_menu()
            choice = input("\nEnter your choice (0-9): ").strip()

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.search_expenses()
            elif choice == '4':
                self.generate_monthly_report()
            elif choice == '5':
                self.view_category_breakdown()
            elif choice == '6':
                self.set_budget()
            elif choice == '7':
                self.export_data()
            elif choice == '8':
                self.view_statistics()
            elif choice == '9':
                self.backup_restore()
            elif choice == '0':
                self._save_data()
                print("\nThank you for using Personal Finance Tracker!")
                break
            else:
                print("Invalid choice!")

    def _print_menu(self):
        print("\n" + "=" * 40)
        print("MAIN MENU")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Monthly Report")
        print("5. Category Breakdown")
        print("6. Budget")
        print("7. Export CSV")
        print("8. Stats")
        print("9. Backup")
        print("0. Exit")
        print("=" * 40)

    def add_expense(self):
        print("\n--- ADD EXPENSE ---")
        try:
            print(f"Categories: {', '.join(VALID_CATEGORIES)}")
            amount = float(input("Amount: "))
            category = input("Category: ").strip().title()
            desc = input("Description: ").strip()
            expense = Expense("", amount, category, desc)  # Auto-date
            self.manager.add_expense(expense)
            self._save_data()
        except ValueError as e:
            print(f"Error: {e}")

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        if not self.manager.expenses:
            print("No expenses yet.")
            return
        for i, e in enumerate(self.manager.expenses, 1):
            print(f"{i}. {e.date} | {e.category} | {e.description} | ₹{e.amount:.2f}")

    def search_expenses(self):
        print("\n--- SEARCH EXPENSES ---")
        keyword = input("Enter keyword/category: ").strip()
        results = self.manager.search_expenses(keyword)
        if not results:
            print("No matching expenses.")
            return
        for i, e in enumerate(results, 1):
            print(f"{i}. {e.date} | {e.category} | {e.description} | ₹{e.amount:.2f}")

    def generate_monthly_report(self):
        print("\n--- MONTHLY REPORT ---")
        ym = input("Enter YYYY-MM (e.g. 2026-03): ").strip()
        report = generate_monthly_report(self.manager, ym)
        print(report)

    def view_category_breakdown(self):
        print("\n--- CATEGORY BREAKDOWN ---")
        breakdown = category_breakdown(self.manager)
        if not breakdown:
            print("No data.")
            return
        total = sum(breakdown.values())
        for cat, amt in breakdown.items():
            pct = (amt / total * 100) if total else 0
            print(f"{cat}: ₹{amt:.2f} ({pct:.1f}%)")

    def set_budget(self):
        print("\n--- SET/UPDATE BUDGET --- (placeholder)")

    def export_data(self):
        print("\n--- EXPORT DATA ---")
        try:
            export_to_csv(self.manager.expenses)
            print("Exported to data/exports/expenses.csv")
        except Exception as e:
            print(f"Export error: {e}")

    def view_statistics(self):
        print("\n--- STATISTICS ---")
        total = sum(e.amount for e in self.manager.expenses)
        count = len(self.manager.expenses)
        avg = total / count if count else 0
        print(f"Total: ₹{total:.2f}, Count: {count}, Average: ₹{avg:.2f}")

    def backup_restore(self):
        print("\n--- BACKUP/RESTORE --- (auto via save_expenses backups)")


def main():
    tracker = FinanceTracker()
    tracker.run()


if __name__ == "__main__":
    main()
