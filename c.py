def calculate_discount(client_name , current_cost):
  if  current_cost>500.0:
     new= current_cost-50.0
  else:
      new=current_cost 
  return new


cdb = [
    {"company": "Stripe", "monthly_cost": 250.50},
    {"company": "Zoom", "monthly_cost": 45.00},
    {"company": "Slack", "monthly_cost": 610.00}
]

for i in cdb:
  a=i['company']
  b=i["monthly_cost"] 
  if b > 500.0:
     d=50
  else:
    d=0 
  x=calculate_discount(a,b)
  print(f"Client {a} received a discount of {d}. New Total: ${x}")
