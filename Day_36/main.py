import requests
import smtplib
import datetime

# Get keys and other info
with open("secret.txt", "r") as file:
    data = file.readlines()


# symbol function
def symbol(percentage):
    return "🔺" if percentage > 0 else "🔻"


EMAIL = data[0]
PASSWORD = data[1]
AV_APIKEY = data[2]
NEWS_APIKEY = data[3]

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"

ALPHAVANTAGE_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_APIKEY,
}

NEWS_PARAMS = {"q": COMPANY_NAME, "pageSize": 3, "page": 1, "apiKey": NEWS_APIKEY}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=ALPHAVANTAGE_ENDPOINT, params=ALPHAVANTAGE_PARAMS)
response.raise_for_status()
stock_info = response.json()["Time Series (Daily)"]

# get date
yesterday = datetime.date.today() - datetime.timedelta(days=1)
day_before_yesterday = datetime.date.today() - datetime.timedelta(days=2)

# get stock closing price for yesterday and the day before
stock_info_1 = float(stock_info[str(yesterday)]["4. close"])
stock_info_2 = float(stock_info[str(day_before_yesterday)]["4. close"])

difference = stock_info_1 - stock_info_2
percentage = round(difference / stock_info_2, 5)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if percentage > 5 or percentage < -5:
    response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    response.raise_for_status()
    news_response = response.json()["articles"]
    news_list = [
        f"{STOCK}: {symbol(percentage).encode('utf-8')}{percentage}% \nHeadline: {news['title'].encode('utf-8')}. \nBrief: {news['description'].encode('utf-8')}."
        for news in news_response
    ]

    # sends email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)

        for news in news_list:
            connection.sendmail(
                from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: Stock Update!\n\n{news}"
            )
