from rawcosts import RawCosts
from demand import Demand
from eoq import EOQ
from scipy.stats import norm
import pandas as pd
import math


def part_02():
    sigma_d = 15
    n = 5  # customers
    L = 2  # weeks
    c = 78
    print("c: {}".format(c))
    h = 0.12
    print("h: {}".format(h))
    CSL = 0.999

    k = norm.ppf(CSL)
    print("k: {}".format(k))

    sigma_dl = sigma_d * math.sqrt(L)
    print("sigma_dl: {}".format(sigma_dl))

    # SS = c * h * k * sigma_dl
    ss = c * h * k * sigma_dl
    print("ss (ind.): {}".format(ss))

    print("ss (tot.): {}".format(ss * n))
    return ss * n


def part_03():
    ss = part_02()
    ss_pooled = ss / math.sqrt(5)
    print("ss (pooled): {}".format(ss_pooled))


part_03()
