from selenium import webdriver
from bs4 import BeautifulSoup
import sqlite3
import time


"""
Main function to execute the scraping script
"""
def main():
    # Connecting to the database
    connection = sqlite3.connect('nadlan-transactions.db')
    cursor = connection.cursor()

    # Setting up target address
    address = input("Insert Address: ").strip()

    # Target address web page
    url = "https://www.nadlan.gov.il/?search=" + address

    interval = time_interval()
    script_automation(connection, cursor, url, interval)


def fetch(connection, cursor, url):
    """
    Fetch the data from the target address

    :param connection: Connection to the nadlan-transactions database
    :type connection: Sqlite3 object
    :param cursor: Cursor object to execute sql commands
    :type cursor: Sqlite3 object
    :param url: The target URL from which scraping data
    :type url: str
    """
    # Setting up chromedriver
    driver = webdriver.Chrome("./chromedriver")
    # Wait for javascript to load
    driver.implicitly_wait(1000)
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.get(url)
    # Loop to keep scrolling the page to load all javascript
    while True:
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
    # Getting all table rows
    rows = soup.findAll("div", class_="tableRow")
    # List to store the formatted values of every row
    res = []
    for row in rows:
        divs = row.findAll("div", class_="tableCol")
        # List to hold the data of every column in a row
        r = []
        for div in divs:
            r.append(div.text.strip())
        res.append(r)

    cursor.execute('''DELETE FROM transactions''')

    # Traversing the results array and populating the database
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


def time_interval():
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
    return time_interval


def script_automation(connection, cursor, url, interval):
    """
    Running the scraping process in automation according to provided time interval

    :param connection: Connection to the nadlan-transactions database
    :type connection: Sqlite3 object
    :param cursor: Cursor object to execute sql commands
    :type cursor: Sqlite3 object
    :param url: The target URL from which scraping data
    :type url: str
    :param interval: Time interval for the script provided by the user
    :type interval: str
    """
    while True:
        fetch(connection, cursor, url)
        print('Database updated')
        # Code for printing out the database
        cursor.execute('''SELECT * FROM transactions''')
        results = cursor.fetchall()
        print(results)
        if interval == '1':
            time.sleep(86400)
        elif interval == '2':
            time.sleep(3600)
        elif interval == '3':
            time.sleep(60)

if __name__ == "__main__":
    main()