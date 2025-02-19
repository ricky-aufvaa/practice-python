website = "https://tpb.rocks/search.html?q=spiderman+no&cat=0"
base_website = "https://tpb.rocks/"
#pip install cinemagoer
#import requests
#from bs4 import BeautifulSoup
#
#URL = website
#r = requests.get(URL)
#
#soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())


import imdb
ia = imdb.Cinemagoer()
movies = ia.search_movie('spiderman')
print(movies)
for movie in movies:
    print(f"ID : {movie.movieID} - Name : {movie['title']} - Year: {movie.get('year', 'Unknown')}")
#print(movies['id'])
