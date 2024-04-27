#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

# from urllib.request import urlopen  # in desktop
# open("_movies.csv", "wb").write(urlopen("https://fondinfo.github.io/data/movies.csv").read())

# import pyodide.http  # in the playground
# open("_movies.csv", "w").writelines(pyodide.http.open_url("https://fondinfo.github.io/data/movies.csv"))

from csv import reader
from operator import itemgetter

def runtime_minutes(runtime: str) -> int:
    total = 0
    for elem in runtime.split():
        n, u = elem[:-1], elem[-1]
        if n.isdecimal():
            total += int(n) * (60 if u == "h" else 1 if u == "m" else 0)
    return total

RANK, TITLE, RUNTIME, ACTORS = 0, 1, 6, 10
actor_runtimes : dict[str, int] = {}
actor_movies : dict[str, list[str]] = {}
actor_collabs : dict[str, set[str]] = {}
with open("_movies.csv") as f:
    r = reader(f)
    head = next(r)
    for m in r:
        if int(m[0]) <= 100:
            for a in m[ACTORS].split(","):
                if a not in actor_movies:
                    actor_movies[a] = []
                    actor_collabs[a] = set()
                    actor_runtimes[a] = 0
                actor_movies[a].append(m[TITLE])
                actor_runtimes[a] += runtime_minutes(m[RUNTIME])
                for a1 in m[ACTORS].split(","):
                    if a1 != a:
                        actor_collabs[a].add(a1)

actors = sorted(actor_runtimes.items(), key=itemgetter(1), reverse=True)[:5]
for a, rt in actors:
    print(a, rt, "\n", actor_movies[a], "\n", actor_collabs[a])
    