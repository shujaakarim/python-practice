import json
order = {"id": "A102", "customer": "Noor Foods", "total": 12800, "paid": False, "notes": None}

order_data = json.dumps(order)
print(order_data)

same_order = json.loads(order_data)
print(same_order["customer"])     # Noor Foods