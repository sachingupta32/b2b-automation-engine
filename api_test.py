# 1. Pull in the web waiter tool we just installed
import requests

print("--- CONNECTING TO LIVE WEB API ---")

# 2. Define the URL of the public web waiter
api_url = "https://jsonplaceholder.typicode.com/users"

# 3. Send a GET request across the internet to fetch data
response = requests.get(api_url)

# 4. Automatically convert the web response into a Python list
live_users = response.json()

print(f"Successfully fetched {len(live_users)} live records from the web!\n")

# 5. Loop through the live web records
for user in live_users:
    name = user["name"]
    city = user["address"]["city"] # Pulling a nested record!

    print(f"User: {name} | Location: {city}")

print("--- LIVE STREAM DATA FETCH COMPLETE ---")
