c_cs = 788  # $
c_ss = 263  # $
c_pi = 0  # $

total_inv_cost = 1051  # $
total_trans_cost = 36000  # $

# CYCLE STOCK COST = $788
# SAFETY STOCK COST = $263
# PIPELINE COST = $0
# Total Inventory Costs = $1051
# Total Transport Costs = $36,000


from scipy.stats import norm
import math

def hadley_whitin(mu_l, sigma_l, mu_d, sigma_d):
    mu_dl = mu_l * mu_d
    sigma_dl = math.sqrt(mu_l * sigma_d ** 2 + mu_d ** 2 * sigma_l ** 2)

    return mu_dl, sigma_dl


def part_02():
    k = norm.ppf(0.99)
    mu_dl, sigma_dl = hadley_whitin(2.0, 1.0, 1.5, 0.25)
    print("mu_dl: {}".format(mu_dl))
    s = mu_dl + k * sigma_dl
    print("s: {}".format(s))


def part_03():
    mu_dl = 3
    ss = 7 - mu_dl
    c = 1750
    h = 0.15
    c_e = c * h
    print(ss * c_e)


def part_04():
    c = 1750
    h = 0.15
    mu_d = 1.5
    L = 2
    c_e = c * h
    print(c_e * mu_d * L)


def part_05():
    print(72 * 400)


def part_07():
    pallets = 72
    loon_trans = 36000 + 1051
    wilson_trans = 28800 + 2626

    print(500 - (loon_trans - wilson_trans) / pallets)

part_07()

# GOING FORWARD, USE THESE COSTS FOR USING LOON HARDWARE FOR TRANSPORTATION:
# CYCLE STOCK COST = $788
# SAFETY STOCK COST = $263
# PIPELINE COST = $0
# Total Inventory Costs = $1051
# Total Transport Costs = $36,000

# GOING FORWARD, USE THESE COSTS FOR USING WILSON EXPRESS FOR TRANSPORTATION:
# CYCLE STOCK COST = $788
# SAFETY STOCK COST = $1050
# PIPELINE COST = $788
# Total Inventory Costs = $2626
# Total Transport Costs = $28,800

