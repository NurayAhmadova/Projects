import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
FUNCTION = "TIME_SERIES_DAILY"

api_key_stocks = "Y22RW9H99Z0I0MQR"
api_key_news = "4ceabcdb5a7a476ab8b04d769fcccac6"


def telegram_bot_sendtext(bot_message):
    bot_token = "1954038233:AAE41ANEN4rdlFsg-Gf_p2yzEK5FJphDyvo"
    bot_chatID = "72636178"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response_tg = requests.get(send_text)

    return response_tg.json()


url = f'https://www.alphavantage.co/query?function={FUNCTION}&symbol={STOCK_NAME}&apikey={api_key_stocks}'
response_stocks = requests.get(url)
data_stocks = response_stocks.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data_stocks.items()]

yesterday_close_price = float(data_list[0]["4. close"])
day_before_yesterday_close_price = float(data_list[1]["4. close"])
difference = yesterday_close_price - day_before_yesterday_close_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_difference = round(difference/yesterday_close_price * 100)
print(abs(percentage_difference))
if abs(percentage_difference) > 1:
    url = f"https://newsapi.org/v2/everything?qInTitle={COMPANY_NAME}&apiKey={api_key_news}"
    response_news = requests.get(url)
    data_news = response_news.json()["articles"][:3]

    formatted_articles_list = [f"Headline: {article['title']} \nBrief: {article['description']}"
                               for article in data_news]
    for article in formatted_articles_list:
        telegram_bot_sendtext(f"{STOCK_NAME}: {up_down}{percentage_difference}% \n{article}")
