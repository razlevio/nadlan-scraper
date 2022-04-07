
# Real Estate Transcations Scraper

Let the user insert an address and a time interval, the scraper will extract all of the real estate transactions in the address provided and save all of the details of the transactions to an SQLite database. The data will be scraped based on the interval; there are three intervals daily, hourly, and minutely which means the data will be pulled every day/hour/minute based on the user input, and the database will be updated accordingly.


## Deployment

To deploy this project you need to do this steps:

    1. Clone the repo and open the project directory
    2. Execute in the terminal: pip install -r requirements.txt
    3. Execute in the terminal: python scraper.py
    4. Insert address and time interval
    5. Stop the automation with CTRL + C / CTRL + Z



[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Frazlevio%2Fscraper&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=&edge_flat=false)](https://hits.seeyoufarm.com)
