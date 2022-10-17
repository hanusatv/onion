import sqlite3
from pathlib import Path

connection = sqlite3.connect('onion.db')

cursor = connection.cursor()

file_create_tables = Path('db/createtables.sql').read_text()

# cursor.executescript(file_create_tables)

connection.commit()


semesters = [
    (1, '2022H', 'Høst 2022'),
    (2, '2023V', 'Vår 2023'),
    (3, '2023H', 'Høst 2023'),
    (4, '2024H', 'Vår 2024'),
    (5, '2024H', 'Høst 2024'),
    (6, '2025H', 'Vår 2025')
]

#cursor.executemany("INSERT INTO semesters VALUES(?,?,?)", semesters)

connection.commit()

cursor.execute("SELECT * FROM semesters")

print(cursor.fetchall())

connection.close()
