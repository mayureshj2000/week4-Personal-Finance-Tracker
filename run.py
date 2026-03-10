
import os
print("Current dir:", os.getcwd())
print("Files:", os.listdir('.'))
print("expense.py exists?", os.path.exists('expense.py'))
from main import main
main()
