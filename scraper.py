# importing required libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import sqlite3
import time

# connecting to the database
connection = sqlite3.connect('nadlan-transactions.db')
cursor = connection.cursor()

# setting up target address and chrome webdriver
address = input("Insert Address: ").strip()
url = "https://www.nadlan.gov.il/?search=" + address  # target address web page


# function to fetch the data from the target address
def fetch():
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.implicitly_wait(1000)  # wait for javascript to load
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.get(url)
    while True: # loop to keep scrolling the page to load all javascript
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(1)
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
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

    cursor.execute('''DELETE FROM transactions''') # deleting records to remove duplications
    # traversing the results array and populating the database
    for values in res:
        sale_date = values[0]
        home_address = values[1]
        block = values[2]
        home_type = values[3]
        rooms = values[4]
        floors = values[5]
        home_size = values[6]
        price = values[7]
        change_in_percent = values[8]
        cursor.execute('''INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?,?)''',
                       (sale_date, home_address, block, home_type, rooms,
                        floors, home_size, price, change_in_percent))
    connection.commit()
    driver.close()
    driver.quit()


# getting the time interval for the script
while True:
    time_interval = input("Fetching interval?\n 1. Daily\n 2. Hourly\n 3. Minutely\n please insert 1,2, or 3\n~ ")
    if time_interval == '1':
        break
    elif time_interval == '2':
        break
    elif time_interval == '3':
        break
    else:
        print("Invalid input")

# script automation
while True:
    fetch()
    print('Database updated')
    # code for printing out the database
    cursor.execute('''SELECT * FROM transactions''')
    results = cursor.fetchall()
    print(results)
    if time_interval == '1':
        time.sleep(86400)
    elif time_interval == '2':
        time.sleep(3600)
    elif time_interval == '3':
        time.sleep(60)