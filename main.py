# # importing required libraries
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import sqlite3
#
#
# def address_processing():
#     address = input("Insert Address: ").strip()
#     return "https://www.nadlan.gov.il/?search=" + address
#
#
# url = address_processing()
# driver = webdriver.Chrome("./chromedriver.exe")
# driver.get(url)
# driver.implicitly_wait(1000)
# content = driver.page_source
# soup = BeautifulSoup(content, 'html.parser')
# rows = soup.findAll("div", class_="tableRow")
#
# con = sqlite3.connect('nadlan.db')
# c = con.cursor()
#
# for row in rows:
#     print("===========================================================")
#     divs = row.findAll("div", class_="tableCol")
#     for div in divs:
#         print(div.text.strip())
#     print("===========================================================")





