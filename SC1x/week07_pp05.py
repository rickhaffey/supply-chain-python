import pandas as pd
from scipy.stats import poisson
import math

# PART 1

l = 4
cost = 100
price = 1100

# data table
demand = list(range(15))
probabilities = [poisson.pmf(d, mu=l) for d in demand]
df = pd.DataFrame(data={
    "demand": demand,
    "probability": probabilities
})
df['cumprob'] = df['probability'].cumsum()

cs = price - cost
ce = cost

cr = cs / (cs + ce)

Q = (df[df['cumprob'] >= cr]).iloc[0]['demand']

print(Q)

# PART 2
# expected profit for possoin dist.:
# (price - g) * (\lambda * P(Q - 1) - Q * P(Q)) + (price - cost) * Q
P_q_1 = poisson.cdf(Q-1, l)
P_q = poisson.cdf(Q, l)

g = 0
profit = (price - g) * (l * P_q_1 - Q * P_q) + (price - cost) * Q
print(profit)


# PART 3
g = 80
ce = cost - g

cr = cs / (cs + ce)

Q = (df[df['cumprob'] >= cr]).iloc[0]['demand']

print(Q)

## Alternate approach calculating a full datatable of
## possible outcomes

def weighted_profit(row, ordered, scenario):
    demand = row['demand']
    sold = min(demand, ordered)
    prob = row['probability']

    if scenario == 'PART1':
        return (price * sold - cost * ordered) * prob
    elif scenario == 'PART3':
        profit = price * sold
        profit -= cost * ordered
        profit += 80 * (ordered - sold) if ordered > sold else 0

        return profit * prob  # for part 3 <<<


o_cols = []
for d in demand:
    col_name = 'o_{}'.format(d)
    o_cols.append(col_name)
    df[col_name] = df.apply(weighted_profit, axis=1, args=[d, 'PART3'])

totals = df.loc[:, o_cols].sum()
max_value = totals.max()

print(df)
print(max_value)
print(totals[totals == max_value])
