import pandas as pd


def run_scenario(price):
    path = '~/Desktop/edX/SC1x/data/W07_PP_Sodatastic{}_data.csv'.format(price)
    data = pd.read_csv(path)
    data['probability'] = data['probability'] / 100.0
    data['CumProb'] = data['probability'].cumsum()

    def weighted_profit(row, ordered, price):
        cost = 6.75
        demand = row['cases']
        sold = min(demand, ordered)
        prob = row['probability']
        return (price * sold - cost * ordered) * prob

    o_cols = []
    for i in range(1, data['cases'].max() + 1):
        col_name = 'o_{}'.format(i)
        o_cols.append(col_name)
        data[col_name] = data.apply(weighted_profit, axis=1, args=[i, price])

    totals = data.loc[:, o_cols].sum()
    max_value = totals.max()

    print("-" * 20)
    print("scenario: price=${}".format(price))
    print(totals[totals == max_value])


run_scenario(24)
run_scenario(20)
