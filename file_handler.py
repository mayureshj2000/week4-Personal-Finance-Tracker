import json
import os
import shutil
from typing import List
from datetime import datetime
from expense import Expense

DATA_FILE = "data/expenses.json"
BACKUP_DIR = "data/backup"
EXPORT_DIR = "data/exports"


def save_expenses(expenses: List[Expense], backup: bool = True) -> None:
    # Ensure directories exist first
    os.makedirs("data", exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)

    try:
        # Save main JSON file
        with open(DATA_FILE, "w") as f:
            json.dump([e.__dict__ for e in expenses], f, indent=2)

        # Optional backup
        if backup:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = os.path.join(BACKUP_DIR, f"expenses_{timestamp}.json")
            shutil.copy(DATA_FILE, backup_path)
    except (IOError, PermissionError) as e:
        raise IOError(f"File save error: {e}")


def load_expenses() -> List[Expense]:
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return [Expense(**item) for item in data]
    except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
        raise ValueError(f"File load error: {e}")


def export_to_csv(expenses: List[Expense], filename: str = "data/exports/expenses.csv") -> None:
    os.makedirs(EXPORT_DIR, exist_ok=True)
    import csv
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "amount", "category", "description"])
        writer.writeheader()
        writer.writerows([e.__dict__ for e in expenses])
