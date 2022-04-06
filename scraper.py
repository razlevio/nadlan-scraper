# importing required libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import sqlite3

address = input("Insert Address: ").strip()
url = "https://www.nadlan.gov.il/?search=" + address  # target address web page
driver = webdriver.Chrome("./chromedriver.exe")
driver.get(url)
driver.implicitly_wait(1000)  # wait for javascript to load
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
rows = soup.findAll("div", class_="tableRow")  # getting all table rows
res = []  # list to store the formatted values of every row
for row in rows:
    divs = row.findAll("div", class_="tableCol")
    r = []  # list to hold the data of every column in a row
    for div in divs:
        r.append(div.text.strip())
    res.append(r)

# connecting to the database
connection = sqlite3.connect('nadlan-transactions.db')
cursor = connection.cursor()

# traversing the results array and populating the database
for values in res:
    sale_date = values[0]
    address = values[1]
    block = values[2]
    home_type = values[3]
    rooms = values[4]
    floors = values[5]
    size = values[6]
    price = values[7]
    change_in_percent = values[8]
    cursor.execute('''INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?,?)''',
                   (sale_date, address, block, home_type, rooms,
                    floors, size, price, change_in_percent))
    connection.commit()

# code for printing out the database
# cursor.execute('''SELECT * FROM data''')
# results = cursor.fetchall()
# print(results)
