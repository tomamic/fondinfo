#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

# import pyodide.http  # in the playground
# open("movies.csv", "w").writelines(pyodide.http.open_url("https://fondinfo.github.io/data/movies.csv"))

from csv import reader
from operator import itemgetter

TITLE, GENRE, ACTORS, DIRECTORS = 1, 4, 10, 11
genres : dict[str, int] = {}
collabs : dict[tuple[str, str], int] = {}
starwars : set[str] = None
with open("movies.csv") as f:
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