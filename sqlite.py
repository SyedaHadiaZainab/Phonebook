import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)''')
c.execute("INSERT INTO test (name) VALUES ('SQLite is working!')")
conn.commit()

c.execute("SELECT * FROM test")
print(c.fetchone())

conn.close()
