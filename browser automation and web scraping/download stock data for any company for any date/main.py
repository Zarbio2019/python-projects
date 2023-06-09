# Author: Zarbio Romulo

import requests
from datetime import datetime
import time

# inputs from console
ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')

# convert datetime to epoch time
from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

# url is obtained from the Download button and copy address
# {ticker}: AAPL
# period1, period2 = time in EPOCH format
url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url, headers=headers).content
# .content: for binary files
# .text: for text files

print(content)
# headers: allow to download from finance.yahoo.com

with open('data.csv', 'wb') as file:
  file.write(content)
# 'wb': write in byte mode
# 'w': write
