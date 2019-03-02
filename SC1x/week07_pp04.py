import pandas as pd
import numpy as np
from scipy.stats import norm
import math


df = pd.read_csv('~/Desktop/edX/SC1x/data/W07_PP_banapple_data.csv',
                 names=['demand', 'probability'],
                 skiprows=1)

df['probability'] = df['probability'] / 100.0
df['cumprob'] = df['probability'].cumsum()
# print(df.head())

cost = 0.30
price = 1.50

# PART 1

# multiples of 50
# max of 500

# what Q to maximize profit?

expected_demand = (df['demand'] * df['probability']).sum()
sigma = math.sqrt((df['demand'] * df['demand'] * df['probability']).sum() - expected_demand ** 2)

cs = price - cost
ce = cost
cr = cs / (cs + ce)

Q = (df[df['cumprob'] >= cr]).iloc[0]['demand']

print("part 1: {}".format(Q))

# PART 2

df['e_short'] = np.where(df['demand'] <= Q, 0, df['demand'] - Q) * df['probability']
expected_short = df['e_short'].sum()
e_daily_profit = (price * expected_demand) - (cost * Q) - (price * expected_short)
e_weekly_profit = round((e_daily_profit * 5) / 50.0) * 50.0

print("part 2: {}".format(e_weekly_profit))

# PART 3

ce = cost + 0.15
cr = cs / (cs + ce)

Q = (df[df['cumprob'] >= cr]).iloc[0]['demand']

print("part 3: {}".format(Q))

# PART 4

df['e_short'] = np.where(df['demand'] <= Q, 0, df['demand'] - Q) * df['probability']
expected_short = df['e_short'].sum()
expected_sold = expected_demand - expected_short

e_daily_profit = (price * expected_sold) - (cost * Q) + (-0.15 * (Q - expected_sold))
e_weekly_profit = round((e_daily_profit * 5) / 50.0) * 50.0

print("part 4: {}".format(e_weekly_profit))
