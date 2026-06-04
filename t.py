# 1. Pull in Python's built-in file scanner tool
import json

def calculate_discount(client_name, current_cost):
    if current_cost > 500.0:
        discount = 50.0
        new_total = current_cost - 50.0
    else:
        discount = 0.0
        new_total = current_cost
    return f"Client {client_name} received a discount of ${discount}. New Total: ${new_total}"

# 2. OPEN THE INDEPENDENT FRUIT BAG (clients.json)
# 'r' means read-only mode
with open('clients.json', 'r') as data_file:
    # 3. SUCK THE JSON DATA DIRECTLY INTO A PYTHON VARIABLE
    cdb = json.load(data_file)

# 4. RUN THE CONVEYOR BELT ON THE LOADED DATA
for i in cdb:
    a = i['company']
    b = i['monthly_cost']
    result_message = calculate_discount(a, b)
    print(result_message)
