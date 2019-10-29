def cels_to_fahr(cels: float) -> float:
    fahr = cels * 1.8 + 32
    return fahr

def main():
    t1 = float(input("Temp (Celsius)? "))
    t2 = cels_to_fahr(t1)
    print(t2)
