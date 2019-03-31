from inventorypolicies.basestock import BaseStock
import pytest


def test_critical_ratio():
    c_s = 25
    c_e = 5
    cr = BaseStock.critical_ratio(c_s, c_e)
    assert cr == pytest.approx(0.833, 0.01)


def test_mean_demand_over_lead_time():
    mean_demand = 100
    lead_time = 2
    mu_dl = BaseStock.mean_demand_over_lead_time(mean_demand, lead_time)
    assert mu_dl == 200


def test_stddev_demand_over_lead_time():
    stddev_demand = 15
    lead_time = 2
    sigma_dl = BaseStock.stddev_demand_over_lead_time(stddev_demand, lead_time)
    assert sigma_dl == pytest.approx(21.2, 0.01)


def test_optimal_base_stock():
    mean_demand = 100
    stddev_demand = 15
    lead_time = 2
    shortage_cost = 25
    excess_cost = 5

    S = BaseStock.optimal_base_stock(mean_demand, stddev_demand, lead_time,
                                     shortage_cost, excess_cost)

    assert S == pytest.approx(220.5, 0.01)
