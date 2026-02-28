import json

# Открываем файл
with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':15} {'Speed':10} {'MTU':5}")
print("-" * 80)

# Проходим по списку imdata
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:50} {descr:15} {speed:10} {mtu:5}")