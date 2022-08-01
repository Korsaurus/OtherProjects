from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
movie_html = response.text

soup = BeautifulSoup(movie_html, "html.parser")
titles = soup.find_all(name="h3", class_="title")
movie_list = [title.text for title in titles]

movie_list.reverse()
with open("movielist.txt", "w", encoding='utf-8') as f:
    for movie in movie_list:
        f.write(movie)
        f.write("\n")
