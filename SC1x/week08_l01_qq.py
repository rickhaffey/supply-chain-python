from eoq import EOQ
from rawcosts import RawCosts
from demand import Demand
from math import sqrt, pi, log

def qq_06():
    c_t = 525
    c_e = 1.25
    rc = RawCosts(unit_cost=1.00, ordering_cost=c_t, holding_cost=c_e, holding_time_unit='M')
    d = Demand(quantity=120, time_unit='M')

    Q = EOQ.optimal_order_quantity(raw_costs=rc, demand=d)
    print("EOQ: {}".format(Q))

    B = 170
    L = 1

    mu_dl = 30
    sigma_dl = 9

    inner_value = (B * d.quantity) / (c_e * sigma_dl * Q * sqrt(2 * pi))
    print("inner value: {}".format(inner_value))

    k = sqrt(2 * log(inner_value))
    print("k: {}".format(k))

    s = mu_dl + k * sigma_dl
    print("s: {}".format(s))


# todo: fix this -- this isn't right
def seek_k(g_k):
    from scipy.stats import norm
    k = 0
    best = (k, norm.ppf(k), abs(norm.ppf(k) - g_k))
    while k <= 1:
        ppf = norm.ppf(k)
        check = (k, ppf, abs(ppf - g_k))
        if check[2] < best[2]:
            best = check
        k += 0.01

    return best


def qq_07():
    Q = 317
    mu_dl = 30
    sigma_dl = 9
    IFR = 0.998
    g_k = (Q / sigma_dl) * (1 - IFR)
    print("G[k]: {}".format(g_k))

    k = 1.09
    print(k)

    s = mu_dl + k * sigma_dl
    print("s: {}".format(s))


def qq_08():
    from scipy.stats import norm
    Q = 317
    mu_dl = 30
    sigma_dl = 9
    c_e = 1.25
    c_s = 75
    D = 120

    p_stockout = (Q * c_e) / (D * c_s)
    k = norm.ppf(1 - p_stockout)
    print(k)

    s = mu_dl + k * sigma_dl
    print(s)

qq_08()