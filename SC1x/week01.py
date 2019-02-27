# Week 01


def w01_mm_pp_01():
    import pandas as pd

    path = '/Users/rhaffey/Desktop/edX/SC1x/data/W01_MM_PP_BostonArt_data.csv'
    df = pd.read_csv(path, names=['part', 'units', 'price'], skiprows=1, index_col=0)

    # ABC segmentation

    df['sales'] = df['price'] * df['units']

    def get_segment(sales):
        if sales > 1000000:
            return 'A'
        elif sales > 200000:
            return 'B'
        else:
            return 'C'

    df['segment'] = df['sales'].apply(get_segment)

    # The company has decided to do this segmentation based on value:
    # type A products are those that bring more than a million dollars in sales per year;
    # type B products are those that bring less than a million but more than $200K in sales per year;and
    # type C are the rest. In the linked file (W01_MM_PP_BostonArt_data.xlsx),
    # you will find the information you need regarding the annual volume of sales per SKU and their price.

    # print(df.head())

    pids = ['PC535850', 'PC412621', 'PC359910', 'PC619194', 'PC151007', 'PC649702', 'PC420169']

    for p in pids:
        segment = df.loc[p]['segment']
        print("{}: {}".format(p, segment))


def w01_mm_pp_02_part2and3():
    from scipy.stats import norm
    wilson = 1.0 - norm.cdf(688, loc=625, scale=225)
    dexter = 1.0 - norm.cdf(693, loc=630, scale=50)
    print("wilson: {}".format(wilson))
    print("dexter: {}".format(dexter))


def w01_mm_pp_02_part4():
    from scipy.stats import poisson
    griffin = 1.0 - poisson.cdf(4, mu=3)
    cody = 1.0 - poisson.cdf(7, mu=6)
    print("griffin: {}".format(griffin))
    print("cody: {}".format(cody))


def w01_pp_kinda_fresh_part03():
    from scipy.stats import norm
    import statistics
    daily_sales = [58, 53, 40, 44, 45, 42, 40]

    mu = statistics.mean(daily_sales)
    sigma = statistics.stdev(daily_sales)

    print("min #: {}".format(norm.ppf(0.97, loc=mu, scale=sigma)))


def w01_pp_kinda_fresh_part04():
    from scipy.stats import poisson

    print("min #: {}".format(poisson.ppf(0.97, mu=2.4)))

