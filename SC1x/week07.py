from scipy.stats import triang
from validation import Validate as v


# Stochastic Demand

# - assumptions: demand, excess demand, planning horizon
# - inventorypolicies charts
# - deterministic vs stochastic
# -


## Three Questions

# 1. How much inventorypolicies on hand (IOH) do I need so P[SO] <= some target service level?
# 2. If I have a certain amount of inventorypolicies on hand, X, what is my P[SO]?
# 3. Given a target service level or IOH, how many units do I expect to sell or be short?

## Demand Distributions

# Empirical
# -- table : demand, frequency, probability, cumulative probability
# -- plot: histogram vs. cumulative %
# -- mean mu [formula]
# -- std dev sigma [formula]
# - concrete example

# Theoretical
# - table
# - notation
# - parameters
# - metrics: mean, median, mode, variance
# - PMF / PDF - formula and plot
# - CDF - formula and plot
# - concrete example

# ## Discrete
# * Discrete Uniform
# * Poisson

# ## Continuous
# * Continuous Uniform
# * Normal
# * Triangle

class TriangleManual:
    """Provides triangle distribution methods with explicit calculations."""

    @staticmethod
    def mean(a, b, c):
        # todo: validation
        return (a + b + c) / 3

    @staticmethod
    def var(a, b, c):
        # todo: validation
        return (a ** 2 + b ** 2 + c ** 2 - a * b - a * c - b * c) / 18

    @staticmethod
    def pdf(x, a, b, c):
        TriangleManual.__validate__(x, a, b, c)

        if a <= x <= c:
            num = 2 * (x - a)
            denom = (b - a) * (c - a)
            return num / denom
        elif c <= x <= b:
            num = 2 * (b - x)
            denom = (b - a) * (b - c)
            return num / denom
        else:
            return 0

    @staticmethod
    def cdf(x, a, b, c):
        TriangleManual.__validate__(x, a, b, c)

        if x < a:
            return 0
        elif a <= x <= c:
            num = (x - a) ** 2
            denom = (b - a) * (c - a)
            return num / denom
        elif c <= x <= b:
            num = (b - x) ** 2
            denom = (b - a) * (b - c)
            return 1 - (num / denom)
        elif x > b:
            return 1

    @staticmethod
    def __validate__(x, a, b, c):
        # todo: revisit these: not always necessary
        # e.g. if x < a or > b, then pdf/cdf evaluate to 0 or 1
        for (var, name) in [(x, "x"), (a, "a"), (b, "b"), (c, "c")]:
            v.required(var, name)

        if a >= b:
            raise ValueError("a must be less than b")

        if c < a or c > b:
            raise ValueError("c must be between a and b")

        if x < a or x > b:
            raise ValueError("x must be between a and b")


class Triangle:

    @staticmethod
    def mean(a, b, c):
        (c, loc, scale) = Triangle.__convert_params__(a, b, c)
        return triang.mean(c, loc=loc, scale=scale)

    @staticmethod
    def var(a, b, c):
        (c, loc, scale) = Triangle.__convert_params__(a, b, c)
        return triang.var(c, loc=loc, scale=scale)

    @staticmethod
    def pdf(x, a, b, c):
        (c, loc, scale) = Triangle.__convert_params__(a, b, c)
        return triang.pdf(x, c, loc=loc, scale=scale)

    @staticmethod
    def cdf(x, a, b, c):
        (c, loc, scale) = Triangle.__convert_params__(a, b, c)
        return triang.cdf(x, c, loc=loc, scale=scale)

    @staticmethod
    def __convert_params__(a, b, c):
        """Converts a, b, and c to c, loc and scale."""
        loc = a
        scale = b - loc
        c_new = (c - loc) / scale
        return c_new, loc, scale


# print(TriangleManual.mean(10, 80, 30))
# print(Triangle.mean(10, 80, 30))
#
# print(TriangleManual.var(10, 80, 30))
# print(Triangle.var(10, 80, 30))
#
# print(TriangleManual.pdf(40, 10, 80, 30))
# print(Triangle.pdf(40, 10, 80, 30))
#
# print(TriangleManual.cdf(40, 10, 80, 30))
# print(Triangle.cdf(40, 10, 80, 30))
#
# print(Triangle.cdf(10, 15, 80, 30))

def critical_ratio(shortage_cost, excess_cost):
    return shortage_cost / (shortage_cost + excess_cost)


class Zahara:
    def __init__(self):
        self.sale_price = 120
        self.cost = 48
        self.salvage_rate = 1 / 3

        # demand
        self.demand_mu = 375
        self.demand_sigma = 220


def pp_zahara_part1():
    z = Zahara()
    cs = z.sale_price - z.cost
    ce = z.cost - (z.sale_price * z.salvage_rate)

    print(critical_ratio(cs, ce))


def pp_zahara_part2():
    from scipy.stats import norm
    z = Zahara()

    cr = 0.9  # from part 1
    print(norm.ppf(q=cr, loc=z.demand_mu, scale=z.demand_sigma))


def pp_zahara_part3():
    from scipy.stats import norm
    z = Zahara()

    cr = 0.9  # from part 1
    k = norm.ppf(cr)
    G_k = norm.pdf(k) - k * (1 - norm.cdf(k))
    expected_short = G_k * z.demand_sigma
    expected_sold = z.demand_mu - expected_short
    print("E[units sold]: {}".format(expected_sold))
    print("E[units short]: {}".format(expected_short))


def expected_profit():
    pass


def pp_zahara_part4():
    # E[units_sold] = E[demand] - E[units short]
    # component 1 (cmp1):
    #   price * E[units_sold]
    # component 2 (cmp2):
    #   cost * Q
    # component 3 (cmp3):
    #   g * (Q - E[units_sold])
    # component 4 (cmp4):
    #   B * E[units short]

    # profit = cmp1 - cmp2 + cmp3 - cmp4
    z = Zahara()

    e_demand = z.demand_mu
    e_short = 10.41549858316587
    e_sold = e_demand - e_short
    price = z.sale_price
    cost = z.cost

    Q = 656.9413444198121
    g = z.sale_price * z.salvage_rate
    B = 0  # no penalty

    profit = (price * e_sold) - (cost * Q) + (g * (Q - e_sold)) - (B * e_short)
    print("profit: {}".format(profit))


def pp_zahara_part7():
    z = Zahara()
    a = 50
    b = 1000
    c = 75

    loc = a
    scale = b - loc
    c_new = (c - loc) / scale

    cr = 0.9  # from part 1

    print(triang.ppf(cr, c=c_new, loc=loc, scale=scale))


def pp_zahara_part8_a(Q=704):
    from scipy.stats import triang

    a = 50
    b = 1000
    c = 75

    loc = a
    scale = b - loc
    c_new = (c - loc) / scale

    expected_short = (1/3) * ((b - Q)**3) / ((b - a) * (b - c))

    mu = triang.mean(c_new, loc=loc, scale=scale)
    expected_sold = mu - expected_short

    print("E[demand]: {}".format(mu))
    print("E[units sold]: {}".format(expected_sold))
    print("E[units short]: {}".format(expected_short))

def pp_zahara_part8_b(Q = 704, e_short=9.83758596491228):
    # E[units_sold] = E[demand] - E[units short]
    # component 1 (cmp1):
    #   price * E[units_sold]
    # component 2 (cmp2):
    #   cost * Q
    # component 3 (cmp3):
    #   g * (Q - E[units_sold])
    # component 4 (cmp4):
    #   B * E[units short]

    # profit = cmp1 - cmp2 + cmp3 - cmp4
    z = Zahara()

    e_demand = 375
    e_sold = e_demand - e_short
    price = z.sale_price
    cost = z.cost

    g = z.sale_price * z.salvage_rate
    B = 0  # no penalty

    profit = (price * e_sold) - (cost * Q) + (g * (Q - e_sold)) - (B * e_short)
    print("profit: {}".format(profit))


pp_zahara_part8_b()
pp_zahara_part8_b(657, 15.307200379326694)

print(23580.993122807013 - 23519.423969653868)