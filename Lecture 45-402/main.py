from bs4 import BeautifulSoup
import requests


with open("100-best-movies.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies][::-1]
print(movie_titles)

with open("movies.txt", "a") as file:
    for title in movie_titles:
        file.write(f"{title}\n")