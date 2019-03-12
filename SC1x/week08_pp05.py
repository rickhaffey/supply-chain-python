from demand import Demand
from rawcosts import RawCosts
from eoq import EOQ
import math
from scipy.stats import norm

D = 13000  # units / yr

# forecast RMSE = 1316 units / yr

L = 2  # weeks
c_t = 1127  # $/order
c = 250  # $/unit
h = 0.1  # $/unit-year

CSL = 0.95


def calc_sigma_dl():
    # use forecast RMSE for sigma_DL
    years_per_week = 1 / 52
    L_conv = L * years_per_week
    sigma_dl = 1316 * math.sqrt(L_conv)  # units / yr
    return sigma_dl


# what IFR would this policy result in?
def part01():
    sigma_dl = calc_sigma_dl()
    g_k = (0.0211 + 0.0206) / 2  # from table

    d = Demand(quantity=D)
    rc = RawCosts(unit_cost=c, ordering_cost=c_t, holding_rate=h)
    Q = EOQ.optimal_order_quantity(rc, d)

    IFR = 1 - ((sigma_dl * g_k) / Q)
    print("IFR: {}".format(IFR))

    return Q


def part02():
    c_e = c * h
    Q = part01()
    sigma_dl = calc_sigma_dl()
    k = norm.ppf(CSL)

    num = c_e * Q * sigma_dl * math.sqrt(2 * math.pi) * math.e ** ((k ** 2) / 2)

    B_1 = num / D
    print("B_1: {}".format(B_1))


def part03():
    Q = part01()
    p_so = 1 - CSL
    c_e = c * h
    c_s = (Q * c_e) / (D * p_so)

    print("c_s: {}".format(c_s))


def part04():
    sigma_dl = calc_sigma_dl()
    g_k = (0.0211 + 0.0206) / 2  # from table using CSL
    Q = part01()

    e_US = sigma_dl * g_k * D / Q
    print("E[US]: {}".format(e_US))


part04()
