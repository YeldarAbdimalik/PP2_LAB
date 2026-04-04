from connect import get_connection

conn = get_connection()
cur = conn.cursor()

# пример вызова функции
cur.execute("SELECT * FROM search_contacts(%s)", ('Ali',))
print(cur.fetchall())

# пример вызова процедуры
cur.execute("CALL upsert_contact(%s, %s)", ('Ali', '99999'))

conn.commit()

cur.close()
conn.close()