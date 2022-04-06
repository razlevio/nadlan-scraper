import sqlite3

connection = sqlite3.connect('nadlan-transactions.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE transactions(sale_date TEXT, address TEXT, block TEXT, home_type TEXT, rooms TEXT, 
floors TEXT, size TEXT, price TEXT, change_in_percent)''')
