from connect import connect
import csv
import json
import os

# ================= INSERT =================
def insert_contact(name, email, birthday, group_name, phone, phone_type):
    conn = connect()
    cur = conn.cursor()

    # group
    cur.execute("SELECT id FROM groups WHERE name=%s", (group_name,))
    group = cur.fetchone()

    if group is None:
        cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (group_name,))
        group_id = cur.fetchone()[0]
    else:
        group_id = group[0]

    # contact
    cur.execute(
        "INSERT INTO contacts(name,email,birthday,group_id) VALUES (%s,%s,%s,%s) RETURNING id",
        (name, email, birthday, group_id)
    )
    contact_id = cur.fetchone()[0]

    # phone
    cur.execute(
        "INSERT INTO phones(contact_id,phone,type) VALUES (%s,%s,%s)",
        (contact_id, phone, phone_type)
    )

    conn.commit()
    cur.close()
    conn.close()


# ================= SELECT =================
def get_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


# ================= SEARCH =================
def find_by_email(email):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts WHERE email ILIKE %s", ('%' + email + '%',))
    print(cur.fetchall())

    cur.close()
    conn.close()


def filter_by_group(group_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, p.phone
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        WHERE g.name=%s
    """, (group_name,))

    print(cur.fetchall())

    cur.close()
    conn.close()


# ================= CSV =================
def insert_from_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            insert_contact(*row)
    print("Import successful")
    


# ================= JSON ================

def export_json(filename):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)

    rows = cur.fetchall()

    data = []

    for r in rows:
        data.append({
            "id": r[0],
            "name": r[1],
            "email": r[2],
            "birthday": str(r[3]) if r[3] else None,  # 💥 FIX HERE
            "group": r[4]
        })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    cur.close()
    conn.close()

    print("Export successful")

def import_json(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        name = item["name"]
        email = item["email"]
        birthday = item["birthday"]
        group_name = item["group"]

        # phone нет в JSON → можно поставить пустое или заглушку
        phone = "000000"
        phone_type = "mobile"

        insert_contact(name, email, birthday, group_name, phone, phone_type)

    conn.commit()
    cur.close()
    conn.close()

    print("Import successful")


# ================= MENU =================
def menu():
    while True:
        print("\n1 Add")
        print("2 Show")
        print("3 Search email")
        print("4 Filter group")
        print("5 Import CSV")
        print("6 Export JSON")
        print("7 Import JSON")
        print("8 Exit")

        ch = input("Choose: ")

        if ch == "1":
            insert_contact(
                input("Name: "),
                input("Email: "),
                input("Birthday YYYY-MM-DD: "),
                input("Group: "),
                input("Phone: "),
                input("Type: ")
            )

        elif ch == "2":
            get_contacts()

        elif ch == "3":
            find_by_email(input("Email: "))

        elif ch == "4":
            filter_by_group(input("Group: "))

        elif ch == "5":
            base_dir = os.path.dirname(__file__)
            file_path = os.path.join(base_dir, "contacts.csv")
            insert_from_csv(file_path)


        elif ch == "6":
            export_json("contacts.json")

        elif ch == "7":
            import_json("contacts.json")

        elif ch == "8":
            break


menu()
