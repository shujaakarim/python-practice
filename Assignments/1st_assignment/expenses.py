import json

expenses_file = "expenses.json"
APPROVAL_LIMIT = 25000
expenses_record = 0

with open(expenses_file, "r") as records:
    expenses = json.load(records)

for expense in expenses:
    expenses_record += 1
print("cafe expenses report" "\n" "Expenses recorded:", expenses_record)

total_price = 0

for expense in expenses:
    total_price += expense["amount"]
print("Total spent:", "RS", total_price)
print("\n")

# add_cate_supply = 0
# what I try to do? I am doing it with a big error??????
#Below code shows what I try to achieve initially
"""
total_amount_supply = 0
total_amount_uti = 0
total_amount_equ = 0
total_amount_mar = 0
total_amount_sta = 0
print("By category:")
for expense in expenses:
    if (
        expense["category"] == "Supplies"
        or expense["category"] == "Utilities"
        or expense["category"] == "Equipment"
        or expense["category"] == "Marketing"
        or expense["category"] == "Staff"
    ):
        total_amount_supply += expense["amount"],"\n"
        total_amount_uti += expense["amount"],"\n"
        total_amount_equ += expense["amount"],"\n"
        total_amount_mar += expense["amount"],"\n"
        total_amount_sta += expense["amount"]
print("Supplies ", "RS", total_amount_supply)
print("Utilities ", "RS", total_amount_supply)
print("Equipment ", "RS", total_amount_supply)
print("Marketing ", "RS", total_amount_supply)
print("Staff ", "RS", total_amount_supply)
"""


# Create an empty dictionary
category_totals = {}

# Calculate the total for each category
for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] += amount

# Display category totals
print("By category:")

for category in category_totals:
    print(" ",category, "Rs", category_totals[category])



