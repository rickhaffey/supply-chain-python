import pandas as pd
import math
import numpy as np

df = pd.read_csv('../data/W09_PP_Curve_Data.csv', index_col=0)


def part01():
    sku = '5487-KW9'
    product = df.loc[sku, :]
    demand = product['demand']
    cost = product['cost']

    print("demand: {}".format(demand))
    print("cost: {}".format(cost))
    print("D_i * c_i: {}".format(demand * cost))
    print("sqrt(D_i * c_i): {}".format(math.sqrt(demand * cost)))


def part02():
    print(sum(np.sqrt(df['demand'] * df['cost'])))


def part03():
    ct_range = (10, 30)
    h_range = (0.15, 0.20)

    smallest = (ct_range[0] / h_range[1])
    largest = (ct_range[1] / h_range[0])

    print("smallest: {}".format(smallest))
    print("largest: {}".format(largest))


def part04_thru_08():
    from functools import reduce

    k = (
            (1 / math.sqrt(2)) *
            (np.sqrt(df['demand'] * df['cost'])).sum()
    )

    ratios = (sorted(
        reduce(list.__add__, [
            [i * 10, i * 100, i * 1000] for i in range(1, 10)
        ])
    ))
    ratios.append(10000)
    ratios.append(25 / 0.15)
    ratios.reverse()

    Ns = [math.sqrt(1 / ratio) * k for ratio in ratios]
    TACSs = [math.sqrt(ratio) * k for ratio in ratios]

    exch_df = pd.DataFrame(data={
        "ct/h": ratios,
        "N": Ns,
        "TACS": TACSs
    })

    print(exch_df)
    print((15000 / k) ** 2)


part04_thru_08()
