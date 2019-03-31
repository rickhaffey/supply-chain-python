import math
from scipy.stats import norm
# Base Stock Inventory Policy

# * one-for-one order policy
# * IP stays constant at Base Stock

# S* (Base Stock) is set based on desired level of service (LOS):
# * via management decision, or
# * using critical ratio


class BaseStock:

    @classmethod
    def critical_ratio(cls, shortage_cost, excess_cost):
        """The service level (probability of not stocking out during the lead-time replenishment
        period) that is optimal for minimizing combined shortage and excess costs."""
        return shortage_cost / (shortage_cost + excess_cost)

    @classmethod
    def optimal_base_stock(cls, mean_demand, stddev_demand, lead_time,
                           shortage_cost, excess_cost):
        # note: assumes all in same time units
        mu_dl = BaseStock.mean_demand_over_lead_time(mean_demand, lead_time)
        sigma_dl = BaseStock.stddev_demand_over_lead_time(stddev_demand, lead_time)
        cr = BaseStock.critical_ratio(shortage_cost, excess_cost)
        k = norm.ppf(cr)
        return mu_dl + k * sigma_dl

    @classmethod
    def mean_demand_over_lead_time(cls, mean_demand, lead_time):
        # NOTE: assumes same time units
        return mean_demand * lead_time

    @classmethod
    def stddev_demand_over_lead_time(cls, stddev_demand, lead_time):
        # NOTE: assumes same time units
        return stddev_demand * math.sqrt(lead_time)
