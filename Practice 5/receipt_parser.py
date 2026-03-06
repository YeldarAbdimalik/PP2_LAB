import re

with open("raw.txt", "r") as file:
    text = file.read()

# Prices
prices = re.findall(r"\d+\.\d{2}", text)
print("Prices:", prices)

# Total
total = sum(map(float, prices))
print("Total:", total)

# Products
products = re.findall(r"([A-Za-z]+)\s\d+\.\d{2}", text)
print("Products:", products)

# Date
date = re.search(r"\d{4}-\d{2}-\d{2}", text)
if date:
    print("Date:", date.group())

# Time
time = re.search(r"\d{2}:\d{2}", text)
if time:
    print("Time:", time.group())

# Payment
payment = re.search(r"(CARD|CASH)", text)
if payment:
    print("Payment:", payment.group())

