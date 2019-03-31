
# based on {variable}
# thresholds: A vs B and B vs C

# output => how many skus in category A?
# - what is the least/most profitable sku in segment A/B/C?
# - in what segment does sku ... fall?
# - what % of total profit is contributed by the top/bottom n% of skus?
# - % of skus and % of revenue in each segment

# - alternate categorization: fast moving / high volatility skus

import pandas as pd
import numpy as np
df = pd.read_csv('./data/W01_L1_QQ4_data.csv', index_col='part_number')

# add a revenue column to segment by
# then sort descending on that col
df['revenue'] = df['price_per_unit'] * df['units_sold']
df.sort_values(by='revenue', ascending=False, inplace=True)

# add a cumulative rev and % of total
df['revenue_cum'] = df['revenue'].cumsum()
df['revenue_cum_pct'] = df['revenue_cum'] / df['revenue'].sum()

# assign segments based on thresholds
df['segment'] = pd.cut(
    df['revenue_cum_pct'],
    bins=[-np.inf, 0.75, 0.95, np.inf],
    labels=['A', 'B', 'C']
)

# segment level metrics
rollup = df.groupby(by='segment').agg({ 'revenue': ['sum', 'count'] })
rollup['revenue', 'pct_of_total'] = rollup['revenue', 'sum'] / rollup['revenue', 'sum'].sum()
print(rollup)



#print(df.head(n=100))