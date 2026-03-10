from typing import Dict
from expense_manager import ExpenseManager

def generate_monthly_report(manager: ExpenseManager, year_month: str) -> str:
    data = manager.monthly_report(year_month)
    total = sum(data.values())
    report = f"Monthly Report ({year_month}): Total ${total:.2f}\n"
    for cat, amt in sorted(data.items(), key=lambda x: x[1], reverse=True):
        pct = (amt / total * 100) if total else 0
        report += f"{cat}: ${amt:.2f} ({pct:.1f}%)\n"
    return report

def category_breakdown(manager: ExpenseManager) -> Dict[str, float]:
    data = {}
    for e in manager.expenses:
        data[e.category] = data.get(e.category, 0) + e.amount
    return dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
