import csv
import os

CSV_FILE = "demo.csv"

# Generate a demo CSV file if not present
demo_data = [
    ["Name", "Group"],
    ["Alice", "Group1"],
    ["Bob", "Group1"],
    ["Charlie", "Group1"],
    ["Dave", "Group2"],
    ["Eve", "Group2"],
    ["Frank", "Group2"]
]
with open(CSV_FILE, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(demo_data)
print(f"Demo CSV file '{CSV_FILE}' has been created.")
