from typing import List, Dict, Optional
from expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses: List[Expense] = []

    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def remove_expense(self, index: int) -> None:
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
        else:
            raise IndexError("Invalid index")

    def search_expenses(self, keyword: str) -> List[Expense]:
        return [e for e in self.expenses if keyword.lower() in e.description.lower() or keyword.lower() == e.category.lower()]

    def monthly_report(self, year_month: str) -> Dict[str, float]:
        monthly = {}
        for e in self.expenses:
            if e.date.startswith(year_month):
                monthly[e.category] = monthly.get(e.category, 0) + e.amount
        return monthly
