from scipy.stats import norm
import math


def part_04():
    a = 50
    b = 0.5
    c = 0.1
    d = 500
    e = 2.2

    dist = 500
    print((d + e * dist - c * dist - a) / b)


part_04()
