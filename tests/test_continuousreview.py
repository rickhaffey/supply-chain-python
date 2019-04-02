from inventorypolicies.continuousreview import SQPolicy
import pytest


def test_mean_demand_over_lead_time():
    mean_demand = 62000  # units / week
    lead_time = 2 / 52  # weeks
    mu_dl = SQPolicy.mean_demand_over_lead_time(mean_demand, lead_time)
    assert mu_dl == pytest.approx(2384.615)


def test_stddev_demand_over_lead_time():
    stddev_demand = 8000  # units / week
    lead_time = 2 / 52  # weeks
    sigma_dl = SQPolicy.stddev_demand_over_lead_time(stddev_demand, lead_time)
    assert sigma_dl == pytest.approx(1568.93)


def test_reorder_point_for_csl():
    mean_demand = 62000
    stddev_demand = 8000
    lead_time = 2 / 52
    csl = 0.95

    s = SQPolicy.reorder_point_for_csl(mean_demand, stddev_demand,
                                       lead_time, csl)

    assert s == pytest.approx(4965.27)


def test_reorder_point_for_cose():
    mean_demand = 62000
    stddev_demand = 8000
    lead_time = 2 / 52
    eoq = 5200
    holding_cost = 100 * 0.15
    csoe = 50000

    s = SQPolicy.reorder_point_for_cose(mean_demand, stddev_demand,
                                        lead_time, eoq, holding_cost, csoe)

    assert s == pytest.approx(5759.17)


def test_reorder_point_for_ifr():
    mean_demand = 62000
    stddev_demand = 8000
    lead_time = 2 / 52
    eoq = 5200
    ifr = 0.99

    s = SQPolicy.reorder_point_for_ifr(mean_demand, stddev_demand,
                                       lead_time, eoq, ifr)

    assert s == pytest.approx(4653.29)


def test_reorder_point_for_cis():
    mean_demand = 62000
    stddev_demand = 8000
    lead_time = 2 / 52
    eoq = 5200
    holding_cost = 100 * 0.15
    shortage_cost = 45

    s = SQPolicy.reorder_point_for_cis(mean_demand, stddev_demand,
                                       lead_time, eoq, holding_cost, shortage_cost)

    assert s == pytest.approx(5383.95)
