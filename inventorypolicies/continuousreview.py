import math
from scipy.stats import norm
from unitnormalloss import UnitNormalLoss


# Order Point, Order Quantity policy

# * Order Q if IP <= s
# * two-bin system


class SQPolicy:
    @classmethod
    def reorder_point_for_csl(cls, mean_demand, stddev_demand, lead_time, csl):
        # Cycle Service Level
        mu_dl = SQPolicy.mean_demand_over_lead_time(mean_demand, lead_time)
        sigma_dl = SQPolicy.stddev_demand_over_lead_time(stddev_demand, lead_time)
        k = norm.ppf(csl)

        return mu_dl + k * sigma_dl

    @classmethod
    def reorder_point_for_cose(cls, mean_demand, stddev_demand, lead_time, eoq,
                               holding_cost, csoe):
        # Cost of Stock Out Event
        mu_dl = SQPolicy.mean_demand_over_lead_time(mean_demand, lead_time)
        sigma_dl = SQPolicy.stddev_demand_over_lead_time(stddev_demand, lead_time)
        k = SQPolicy.__k_csoe__(csoe, mean_demand, holding_cost, eoq, sigma_dl)

        return mu_dl + k * sigma_dl

    @classmethod
    def reorder_point_for_ifr(cls, mean_demand, stddev_demand, lead_time, eoq, ifr):
        # Item Fill Rate
        mu_dl = SQPolicy.mean_demand_over_lead_time(mean_demand, lead_time)
        sigma_dl = SQPolicy.stddev_demand_over_lead_time(stddev_demand, lead_time)
        g_k = SQPolicy.__g_k_ifr__(eoq, sigma_dl, ifr)

        # Solve k from g_k
        k = UnitNormalLoss.loss_inverse(g_k)
        return mu_dl + k * sigma_dl

    @classmethod
    def reorder_point_for_cis(cls, mean_demand, stddev_demand, lead_time, eoq,
                              holding_cost, shortage_cost):
        # Cost per Item Short
        mu_dl = SQPolicy.mean_demand_over_lead_time(mean_demand, lead_time)
        sigma_dl = SQPolicy.stddev_demand_over_lead_time(stddev_demand, lead_time)
        k = SQPolicy.__k_cis__(eoq, holding_cost, shortage_cost, mean_demand)

        return mu_dl + k * sigma_dl

    @classmethod
    def __g_k_ifr__(cls, eoq, sigma_dl, ifr):
        return (eoq / sigma_dl) * (1 - ifr)

    @classmethod
    def __k_csoe__(cls, csoe, mean_demand, excess_cost, eoq, sigma_dl):
        num = csoe * mean_demand
        denom = excess_cost * eoq * sigma_dl * math.sqrt(2 * math.pi)

        # todo: better handling of this preliminary check
        if num / denom > 1:
            return math.sqrt(2 * math.log(num / denom))
        else:
            return math.nan

    @classmethod
    def __k_cis__(cls, eoq, holding_cost, shortage_cost, mean_demand):
        value = (eoq * holding_cost) / (mean_demand * shortage_cost)

        # todo: better handling of this preliminary check
        if value <= 1:
            return norm.ppf(1 - value)
        else:
            return math.nan

    @classmethod
    def mean_demand_over_lead_time(cls, mean_demand, lead_time):
        # NOTE: assumes same time units
        return mean_demand * lead_time

    @classmethod
    def stddev_demand_over_lead_time(cls, stddev_demand, lead_time):
        # NOTE: assumes same time units
        return stddev_demand * math.sqrt(lead_time)
