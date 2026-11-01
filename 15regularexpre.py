import re

email = input("Enter email: ")
phone = input("Enter phone number: ")
log = input("Enter transaction log: ")

if re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email):
    print("Valid Email")
else:
    print("Invalid Email")

if re.match(r'^[6-9]\d{9}$', phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

ids = re.findall(r'TXN\d+', log)
print("Transaction IDs:", ids)