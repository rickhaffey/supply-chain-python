# Based on historical data, you have determined the daily
# demand for bottled water in Kendall during the summer
# is – on average – normally distributed with a mean of
# 400 bottles, with a standard deviation of 100 bottles.
# The store buys the water bottles at 55 cents a piece,
# and spends an additional 10 cents in electricity and ice
# to chill it and keep it that way. A chilled bottle is sold
# to the tourists at 1 dollar a piece. Since the labels of
# the bottles deteriorate under water, the bottles that do
# not sell at the end of the day have to be discarded at a loss.

# How many water bottles should the store prepare for sale every
# day? Round to the closest multiple of 10.

from scipy.stats import norm

# part 1

# demand ~ N(400, 100)
mu = 400
sigma = 100
price = 1.00
cost = 0.55 + 0.10

cs = price - cost
ce = cost

cr = cs / (ce + cs)

k = norm.ppf(cr)

Q = mu + k * sigma
print(Q)

# part 2

G_k = norm.pdf(k) - k * (1 - norm.cdf(k))
expected_short = G_k * sigma
profit = price * mu - cost * Q  - price * expected_short
print(profit)

# part 3
cs = cs + 0.50
cr = cs / (cs + ce)

k = norm.ppf(cr)

Q = mu + sigma * k
print(Q)

# part 4
cs = price - cost + 0.50
ce = cost + 0.10 - 0.65

cr = cs / (ce + cs)
k = norm.ppf(cr)
Q = mu + k * sigma
print(Q)

cost = cost + 0.10
g = 0.65

