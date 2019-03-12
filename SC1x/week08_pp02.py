# Order Point, Order Quantity Policy

import math


def part02():
    sigma_d = 70
    L = 0.5

    sigma_dl = sigma_d / math.sqrt(2)
    print(sigma_dl)
    return sigma_dl


def part03():
    from scipy.stats import norm
    CSL = 0.9
    k = norm.ppf(CSL)
    print("k: {}".format(k))
    return k


def part04():
    k = part03()
    mu_d = 240
    sigma_d = 70
    L = 0.5

    s = (mu_d * L) + k * part02()
    print("s: {}".format(s))


def part05():
    Q = 310
    c = 50
    c_e = 0.01 * c

    monthly_cost = c_e * Q / 2
    annual_cost = monthly_cost * 12
    print(annual_cost)


def part06():
    c = 50
    c_e = 0.01 * c
    k = part03()
    sigma_dl = part02()

    print(c_e * k * sigma_dl * 12)


def part07():
    D = 240
    L = 0.5
    c = 50
    h = 0.06 / 12
    c_e = c * h
    pipeline_inv = D * L
    print(pipeline_inv * c_e)


part07()
