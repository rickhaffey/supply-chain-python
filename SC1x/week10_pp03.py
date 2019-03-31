import math
from scipy.stats import norm

L = 2  # weeks
c = 1750  # $ / pallet
Q = 6  # pallets
mu_d = 1.5  # pallets / week
sigma_d = 0.25  # pallets
h = 0.15
CSL = 0.99
c_tr = 500  # $ / pallet

c_e = h * c


def part_01():
    print(c_e * (Q / 2))


def part_02():
    mu_dl = mu_d * L
    sigma_dl = sigma_d * math.sqrt(L)
    k = norm.ppf(CSL)

    print(mu_dl + k * sigma_dl)
    print("mu_dl: {}".format(mu_dl))
    print("sigma_dl: {}".format(sigma_dl))
    print("k: {}".format(k))

    return k * sigma_dl


def part_03():
    s = 4
    mu_dl = 3
    ss = s - mu_dl
    print(c_e * ss)


def part_04():
    0  # no cost until delivery, so 0 pipeline inv cost


def part_05():
    pallets = mu_d * 48
    print(pallets * c_tr)


part_01()


# GOING FORWARD, USE THESE COSTS FOR USING LOON HARDWARE FOR TRANSPORTATION:
# CYCLE STOCK COST = $788
# SAFETY STOCK COST = $263
# PIPELINE COST = $0
# Total Inventory Costs = $1051
# Total Transport Costs = $36,000