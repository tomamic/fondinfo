double f(double x) {
    return x * x + x;
}

double integral(double a, double b, int64_t n) {
    auto total = 0.0;
    auto dx = (b - a) / n;
    for (auto i = 0; i < n; ++i) {
        total += dx * f(a + dx * i);
    }
    return total;
}
