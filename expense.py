from dataclasses import dataclass
from datetime import datetime
from typing import List

VALID_CATEGORIES = ["Food", "Transport", "Entertainment", "Utilities", "Shopping", "Other"]

@dataclass
class Expense:
    date: str
    amount: float
    category: str
    description: str

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be positive")
        if self.category not in VALID_CATEGORIES:
            raise ValueError(f"Category must be one of {VALID_CATEGORIES}")
        if not self.date:
            self.date = datetime.now().strftime("%Y-%m-%d")
