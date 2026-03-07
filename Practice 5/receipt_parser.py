import re
import json


with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()



date_time = re.search(r"Время:\s*([\d\.]+\s[\d:]+)", text)
date_time = date_time.group(1) if date_time else None



payment = re.search(r"(Банковская карта|Наличные)", text)
payment = payment.group(1) if payment else None



total = re.search(r"ИТОГО:\s*\n([\d\s,]+)", text)
total = total.group(1).strip() if total else None



pattern = r"\d+\.\n(.+?)\n([\d,]+)\s*x\s*([\d\s,]+)\n([\d\s,]+)"

items = []

for match in re.findall(pattern, text):
    name, qty, price, total_price = match

    items.append({
        "name": name.strip(),
        "quantity": qty,
        "price": price,
        "total": total_price
    })


receipt = {
    "datetime": date_time,
    "payment_method": payment,
    "total_amount": total,
    "items": items
}



with open("receipt.json", "w", encoding="utf-8") as f:
    json.dump(receipt, f, indent=4, ensure_ascii=False)


print("Receipt parsed successfully!")