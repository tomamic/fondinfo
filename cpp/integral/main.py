import cppyy, time
cppyy.include("integral.h")
from cppyy.gbl import integral

def py_f(x: float) -> float:
    return x * x + x

def py_integral(a: float, b: float, n: int) -> float:
    total = 0.0
    dx = (b - a) / n
    for i in range(n):
        total += dx * py_f(a + dx * i)
    return total

def main():
    t0 = time.time()
    i = integral(3, 4, 100_000_000)
    t = time.time() - t0
    print(f"C++\t{i:8.4f}\t{t:8.4f}")

    t0 = time.time()
    i = py_integral(3, 4, 100_000_000)
    t = time.time() - t0
    print(f"Python\t{i:8.4f}\t{t:8.4f}")

main()
