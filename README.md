# Real Estate Transcations Scraper

Let the user insert an address and a time interval, the scraper will extract all of the real estate transactions in the address provided and save all of the details of the transactions to an SQLite database. The data will be scraped automatically based on the interval provided; there are three intervals daily, hourly, and minutely which means the data will be pulled every day/hour/minute based on the user input, and the database will be updated accordingly.


## Deployment

To deploy this project you need to do this steps:

   1. Clone the repo and open the project directory
   2. Execute in the terminal: pip install -r requirements.txt
   3. [Download](https://sites.google.com/chromium.org/driver/donloads) the last version of chromedriver for your own operating system
   4. Put the chromedriver in the folder under the name chromedriver 
   5. Execute in the terminal: python scraper.py
   6. Insert address and time interval
   7. Stop the automation with CTRL + C / CTRL + Z
