from urllib.request import urlopen
from re import sub

puzzles = [("5x5", "15266"),
           ("6x6", "16075"),
           ("8x8", "21330"),
           ("9x9", "168142"),
           ("12x12", "29512"),
           ("15x15", "2564")]

for size, number in puzzles:
    text = ""
    url = f"http://www.menneske.no/hitori/{size}/eng/utskrift.html?number={number}"
    url = sub(r"9x9/", "", url)
    print(url)
    with urlopen(url) as r, open(f"hitori-{size}-{number}.txt", "w") as w:
        text = r.read().decode("utf-8")
        text = sub(r"[\s,]+", "", text)
        text = sub(r".*<table>", "", text)
        text = sub(r"</table>.*", "", text)
        text = sub(r"</td></tr>", "\n", text)
        text = sub(r"</td>", ",", text)
        text = sub(r"[^\d,\n]", "", text)
        print(text, file=w)
