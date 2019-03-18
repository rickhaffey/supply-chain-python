import pandas as pd
from rawcosts import RawCosts
from demand import Demand
from eoq import EOQ
import math
import numpy as np
from scipy.stats import norm

df = pd.read_csv('../data/W09_PP_CurveSafety_Data.csv', index_col=0)
# print(df)

h = 0.15
c_t = 25


def part01():
    sku = '3206-BO1'
    item = df.loc[sku]

    rc = RawCosts(unit_cost=item['cost'], ordering_cost=c_t, holding_rate=h)
    d = Demand(quantity=item['demand'])
    Q = EOQ.optimal_order_quantity(rc, d)

    print("Q: {}".format(Q))
    sigma = item['rmse']
    print("sigma: {}".format(sigma))
    print("sigma_dl: {}".format(sigma * math.sqrt(1 / 12)))


def part02():
    sku = '3206-BO1'
    item = df.loc[sku]

    cost = item['cost']
    demand = item['demand']

    rc = RawCosts(unit_cost=cost, ordering_cost=c_t, holding_rate=h)
    d = Demand(quantity=demand)
    Q = EOQ.optimal_order_quantity(rc, d)

    sigma = item['rmse']
    sigma_dl = sigma * math.sqrt(1 / 12)

    print("sigma_dl * ci: {}".format(sigma_dl * cost))
    print("D/Q: {}".format(demand / Q))
    print("(D/Q) * (sigma_dl * ci): {}".format((demand / Q) * sigma_dl * cost))


def calc_eoq(row):
    cost = row['cost']
    demand = row['demand']

    rc = RawCosts(unit_cost=cost, ordering_cost=c_t, holding_rate=h)
    d = Demand(quantity=demand)
    return EOQ.optimal_order_quantity(rc, d)


def part03():
    df['sigma_dl'] = df['rmse'] * math.sqrt(1/12)
    df['eoq'] = df.apply(calc_eoq, axis=1)
    df['vis'] = (df['demand'] / df['eoq']) * df['sigma_dl'] * df['cost']

    print("sum of sigma_dl * ci: {}".format(sum(df['sigma_dl'] * df['cost'])))
    print('sum of D/Q: {}'.format(sum(df['demand'] / df['eoq'])))
    print('sum of vis: {}'.format(sum(df['vis'])))


def part04():
    part03()  # generate intermediate columns
    k = norm.ppf(0.85)
    G_k = 0.07795

    tss = sum(k * df['sigma_dl'] * df['cost'])
    tvis = sum((df['demand'] / df['eoq']) * df['cost'] * df['sigma_dl'] * G_k)

    print("TSS: {}".format(tss))
    print("TVIS: {}".format(tvis))

#part03()
#print(df)

part04()

