from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_index = article_upvotes.index(max(article_upvotes))

popular_text = article_texts[max_index]
popular_link = article_links[max_index]
max_upvote = article_upvotes[max_index]

print(popular_text)
print(popular_link)
print(max_upvote)
