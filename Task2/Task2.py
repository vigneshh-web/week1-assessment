import csv
import json
import os
from dotenv import load_dotenv
import requests

employees = []
high_earners = []

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        employees.append(row)

        if int(row["salary"]) > 50000:
            high_earners.append(row)


with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

with open("high_earners.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())

    writer.writeheader()
    writer.writerows(high_earners)

print("Rows read:", len(employees))
print("High earners:", len(high_earners))

load_dotenv()

api_key = os.getenv("API_KEY")

print("API Key:", api_key)


url = "https://jsonplaceholder.typicode.com/users"
urls = "https://jsonplaceholder.typicode.com/users/9999"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    users = response.json()

    for user in users[:3]:
        print(user["id"], "-", user["name"], "-", user["email"])

    responses = requests.get(urls, timeout=5)
    responses.raise_for_status()

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the server")

except requests.exceptions.HTTPError:
     print(f"/users/9999 -> {responses.status_code} Not found")

user_details = []
response = requests.get(url, timeout=5)
response.raise_for_status()
users = response.json()
for user in users:
    details = {
        "id": user.get("id"),
        "name": user.get("name"),
        "city": user.get("address", {}).get("city"),
        "company": user.get("company", {}).get("name")
    }
    user_details.append(details)

with open("users.json", "w") as file:
    json.dump(user_details, file, indent=4)

print("User details saved successfully!")