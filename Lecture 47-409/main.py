from bs4 import BeautifulSoup
import requests
import smtplib

port = 587
password = "PYTHON123"
sender_email = "python.test.n.a@gmail.com"
buy_price = 728


url = "https://www.amazon.com/Dyson-Airwrap-Styler-Shape/dp/B07MN2NBTT/ref=sr_1_1?crid=FLC9H958C1HR&dchild=1&" \
      "keywords=dyson+airwrap&qid=1630602400&sprefix=dyson+air+purifier%2Caps%2C358&sr=8-1"
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
}
response = requests.get(url=url,
                        headers=headers)
response_html = response.text

soup = BeautifulSoup(response_html, 'html.parser')
price_with_currency = soup.find(name="span", id="priceblock_ourprice").getText()
price_raw = float(price_with_currency.split("$")[1])
product_name = soup.find(name="span", id="productTitle").getText().strip()


if price_raw <= buy_price:
    with smtplib.SMTP("smtp.gmail.com", port=port) as connection:
        text = f"{product_name} is now {price_raw}\n{url}"
        connection.starttls()
        connection.login(sender_email, password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=sender_email,
                            msg=f"Subject: Amazon Price Alert!\n\n{text}"
                            )
