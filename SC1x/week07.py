from scipy.stats import triang
from validation import Validate as v


# Stochastic Demand

# - assumptions: demand, excess demand, planning horizon
# - inventory charts
# - deterministic vs stochastic
# -


## Three Questions

# 1. How much inventory on hand (IOH) do I need so P[SO] <= some target service level?
# 2. If I have a certain amount of inventory on hand, X, what is my P[SO]?
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


print(TriangleManual.mean(10, 80, 30))
print(Triangle.mean(10, 80, 30))

print(TriangleManual.var(10, 80, 30))
print(Triangle.var(10, 80, 30))

print(TriangleManual.pdf(40, 10, 80, 30))
print(Triangle.pdf(40, 10, 80, 30))

print(TriangleManual.cdf(40, 10, 80, 30))
print(Triangle.cdf(40, 10, 80, 30))

print(Triangle.cdf(10, 15, 80, 30))