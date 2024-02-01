import sqlite3

connection = sqlite3.connect('/Users/user/Desktop/Python/Datas/SQL/chinook.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM customer LIMIT 5;')
print(cursor.fetchall())
connection.close()