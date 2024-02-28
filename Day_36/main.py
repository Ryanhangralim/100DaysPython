import requests
import smtplib
import datetime

# Get keys and other info
with open("secret.txt", "r") as file:
    data = file.readlines()

EMAIL = data[0]
PASSWORD = data[1]
AV_APIKEY = data[2]
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"

ALPHAVANTAGE_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : AV_APIKEY,
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=ALPHAVANTAGE_ENDPOINT, params=ALPHAVANTAGE_PARAMS)
response.raise_for_status()
stock_info = response.json()["Time Series (Daily)"]

#get date
yesterday = datetime.date.today() - datetime.timedelta(days = 1)
day_before_yesterday = datetime.date.today() - datetime.timedelta(days = 2)

#get stock closing price for yesterday and the day before
stock_info_1 = stock_info[str(yesterday)]["4. close"]
stock_info_2 = stock_info[str(day_before_yesterday)]["4. close"]

print(stock_info_1)
print(stock_info_2)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

