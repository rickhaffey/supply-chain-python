price = 160
g = 60
cost = 100
expected_demand = 200


# triang
a = 100
b = 250
c = 200

# PART 2

from scipy.stats import norm

cs = price - cost
ce = cost - g

cr = cs / (cs + ce)

k = norm.ppf(cr)

Q2 = 220 + k * 30
print(Q2)


# PART 3
Q3 = cr * 300
print(Q3)


# PART 4
loc = 0
scale = 300
from scipy.stats import uniform
Q4 = uniform.ppf(0.20, loc=loc, scale=scale)
print(Q4)