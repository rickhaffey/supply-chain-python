import math

mu_d = 240  # units / mo
sigma_d = 70  # units / mo
L = 0.5  # mo
k = 1.28  # set based on CSL


# what is S?
def part01():
    R = 2  # mo
    RL = R + L
    mu_dlr = mu_d * RL
    sigma_dlr = sigma_d * math.sqrt(RL)
    s = mu_dlr + k * sigma_dlr
    print("s: {}".format(s))
    return s


# what is Q?
def part02():
    R = 2  # mo
    Q = mu_d * R
    print("Q: {}".format(Q))
    return Q


# what is T & t_c * T
def part03():
    R = 2  # mo
    T = 12 / R
    print("T: {}".format(T))
    print("cost: {}".format(T * 100))


part03()
