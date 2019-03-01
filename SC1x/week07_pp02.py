import pandas as pd

demand = pd.read_csv('~/Desktop/edX/SC1x/data/W07_PP_Sodatastic24_data.csv')
demand['probability'] = demand['probability'] / 100.0
demand['CumProb'] = demand['probability'].cumsum()


def weighted_profit(row, ordered):
    price = 24
    cost = 6.75
    demand = row['cases']
    sold = min(demand, ordered)
    prob = row['probability']
    return (price * sold - cost * ordered) * prob


o_cols = []
for i in range(1, demand['cases'].max() + 1):
    col_name = 'o_{}'.format(i)
    o_cols.append(col_name)
    demand[col_name] = demand.apply(weighted_profit, axis=1, args=[i])

totals = demand.loc[:, o_cols].sum()
max_value = totals.max()

print(totals[totals == max_value])

# >>> o_16    188.112