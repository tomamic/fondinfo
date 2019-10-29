class MeteoStation:
    def __init__(self, name: str):
        self._name = name
        self._rain = []

    def add(self, day: str, val: int) -> None:
        pair = day, val
        self._rain.append(pair)

    def total_rain(self, day1: str, day2: str) -> int:
        total = 0
        for pair in self._rain:
            day, val = pair[0], pair[1]
            if day1 <= day <= day2:
                total += val
        return total

def main():
    with open("my_station.txt", "w") as f0:
        f0.write("2019-10-17 1\n2019-10-18 2\n2019-10-15 12\n2019-10-20 7\n")

    station = MeteoStation("My station")
    with open("my_station.txt", "r") as f:
        for line in f:
            parts = line.split(" ")
            day = parts[0]
            val = int(parts[1])
            station.add(day, val)

    print(station.total_rain("2019-10-15", "2019-10-17"))

main()
