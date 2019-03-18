from scipy.stats import poisson
import pandas as pd


def part_01():
    cdf = poisson.cdf(0, 0.5)

    print("cdf: {}".format(cdf))


def part_02():
    cdf = 1 - poisson.cdf(2, 0.5)
    print("cdf: {}".format(cdf))


def part_03():
    lmbda = 0.5
    demand = list(range(9))
    pmf = list(poisson.pmf(x, lmbda) for x in demand)
    cdf = list(poisson.cdf(x, lmbda) for x in demand)

    df = pd.DataFrame(data={
        'demand': demand,
        'p[x]': pmf,
        'F[x]': cdf
    })
    print(df)

    csl = 0.9
    s = (df[df['F[x]'] >= csl]).iloc[0]['demand']
    print("\ns: {}".format(s))

    return lmbda, df, s


def part_04():
    lmbda, df, s = part_03()
    loss_x = [lmbda - df.loc[0, 'demand']]

    for i in range(1, 9):
        loss_x.append(
            loss_x[i - 1] -
            (df.loc[i, 'demand'] - df.loc[i - 1, 'demand']) *
            (1 - df.loc[i - 1, 'F[x]'])
        )

    df['L[x]'] = loss_x
    print(df)

    Q = 2
    IFR = 1 - (df.loc[s, 'L[x]'] / Q)
    print("IFR: {}".format(IFR))


part_04()
