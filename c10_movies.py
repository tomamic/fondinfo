#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def download(url, name):
    try:
        from pyodide.http import open_url  # in the playground
        open(name, "w").write(open_url(url).read())
    except:
        from urllib.request import urlopen  # locally
        open(name, "wb").write(urlopen(url).read())

from os.path import isfile
if not isfile("_movies.csv"):
    download("https://fondinfo.github.io/data/movies.csv", "_movies.csv")

from csv import reader
from operator import itemgetter

TITLE, GENRE, ACTORS, DIRECTORS = 1, 4, 10, 11
genres : dict[str, int] = {}
collabs : dict[tuple[str, str], int] = {}
starwars : set[str] = None
with open("_movies.csv", encoding="utf-8") as f:
    r = reader(f)
    head = next(r)
    for m in r:
        movie_genres = m[GENRE].split(",")
        for g in movie_genres:
            genres[g] = genres.get(g, 0) + 1

        movie_directors = m[DIRECTORS].split(",")
        movie_actors = m[ACTORS].split(",")
        for d in movie_directors:
            d = d.split("(")[0]
            for a in movie_actors:
                k = (d, a)
                collabs[k] = collabs.get(k, 0) + 1

        if "Star Wars" in m[TITLE]:
            if starwars == None:
                starwars = set(movie_actors)
            else:
                starwars &= set(movie_actors)

genres_list = sorted(genres.items(), key=itemgetter(-1), reverse=True)
collabs_list = sorted(collabs.items(), key=itemgetter(-1), reverse=True)[:10]

print("Genres")
for k, v in genres_list:
    print(k, v)

print("\nCollabs")
for k, v in collabs_list:
    print(k, v)

print("\nStar Wars cast\n", starwars)
