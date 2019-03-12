from scipy.stats import norm
import math

mu_d = 240  # units / mo
c_e = 0.25  # $ / unit-mo
c_s = 5  # $ / unit

# (R,S) policy
R = 2  # mo
Q = 480  # units


# find k that produces c_s = $5
def part01():
    D = Q / R
    p_so = (Q * c_e) / (D * c_s)
    print("P[SO]: {}".format(p_so))

    k = norm.ppf(1 - p_so)
    print("k: {}".format(k))

    return k


# find G(k) for given k
def part02():
    k = part01()
    g_k = 0.0475  # from table lookup
    print("G(k): {}".format(g_k))
    return g_k


def part03():
    L = 0.5  # mo
    sigma_d = 70  # units / mo
    RL = R + L
    sigma_dlr = sigma_d * math.sqrt(RL)
    print("sigma_dlr: {}".format(sigma_dlr))
    g_k = part02()
    print("E[US]: {}".format(sigma_dlr * g_k))
    return sigma_dlr


def part04():
    cycles = 12 / R
    print("order cycles: {}".format(cycles))
    sigma_dlr = part03()
    g_k = part02()
    cost = c_s * sigma_dlr * g_k * cycles
    print("cost: {}".format(cost))


part04()
