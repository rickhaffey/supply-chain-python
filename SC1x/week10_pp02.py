from scipy.stats import norm
import math


def hadley_whitin(mu_l, sigma_l, mu_d, sigma_d):
    mu_dl = mu_l * mu_d
    sigma_dl = math.sqrt(mu_l * sigma_d ** 2 + mu_d ** 2 * sigma_l ** 2)

    return mu_dl, sigma_dl


mu_l = 4  # weeks
sigma_l = 1  # weeks

mu_d = 32  # units/week
sigma_d = 12  # units/week

c = 100000
h = 0.22
c_e = c * h

csl = 0.95
k = norm.ppf(csl)


def part_01():
    p1_A = c_e * mu_d * mu_l
    print("p1_A E[$ PI]: {} M".format(p1_A / 10 ** 6))

    mu_dl, sigma_dl = hadley_whitin(mu_l, sigma_l, mu_d, sigma_d)
    p1_B = c_e * k * sigma_dl
    print('p1_b E[$SS]: {} M'.format(p1_B / 10 ** 6))

    return round(p1_A, 2), round(p1_B, 2)


def part_02():
    mu_l = 5
    sigma_l = 0.5

    p2_A = c_e * mu_d * mu_l
    mu_dl, sigma_dl = hadley_whitin(mu_l, sigma_l, mu_d, sigma_d)
    p2_B = c_e * k * sigma_dl

    print("p2_A E[$ PI]: {} M".format(p2_A / 10 ** 6))
    print('p2_b E[$SS]: {} M'.format(p2_B / 10 ** 6))

    return round(p2_A, 2), round(p2_B, 2)


def part_03():
    pi, ss = part_01()
    first = pi + ss

    pi, ss = part_02()
    second = pi + ss

    print((second - first) / 1664)


part_03()
