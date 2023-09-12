from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200611015421/https://www.empireonline.com/movies/features/best-tv-shows-ever-2/"
# Extracting titles and links of the articles

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
#print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="title")
#print(all_movies)

movie_titles = [movie.getText() for movie in all_movies]
# for n in range(len(movie_titles) -1, -1, -1):
#     print(movie_titles[n])

movies = movie_titles[::-1]  # to reverse the list [::-1]

# create a text with all movie names
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")