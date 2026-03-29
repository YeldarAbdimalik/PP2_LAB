#insert


from connect import connect

def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

insert_contact("Ali", "87001111111")
insert_contact("Dana", "87002222222")
insert_contact("Eldar", "87003333333")
insert_contact("Aruzhan", "87004444444")


#select
 
def get_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

#update

def update_phone(name, new_phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET phone=%s WHERE name=%s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()

#delete

def delete_contact(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE name=%s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()

#find name

def find_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE name ILIKE %s",
        ('%' + name + '%',)
    )

    print(cur.fetchall())

#find by phone
def find_by_phone(prefix):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE phone LIKE %s",
        (prefix + '%',)
    )

    print(cur.fetchall())

#csv

import csv
from connect import connect

def insert_from_csv(file):
    conn = connect()
    cur = conn.cursor()

    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()

#menu

def menu():
    while True:
        print("1. Add contact")
        print("2. Show contacts")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            get_contacts()

        elif choice == "3":
            name = input("Name: ")
            phone = input("New phone: ")
            update_phone(name, phone)

        elif choice == "4":
            name = input("Name: ")
            delete_contact(name)

        elif choice == "5":
            break



