import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
''')

cursor.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
               ('Saad', 'saad@example.com', 25))
cursor.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
               ('Ali', 'ali@example.com', 30))
conn.commit()

cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute('UPDATE users SET age = ? WHERE name = ?', (26, 'Saad'))
conn.commit()

cursor.execute('DELETE FROM users WHERE name = ?', ('Ali',))
conn.commit()

conn.close()
print('Database operations completed!')
