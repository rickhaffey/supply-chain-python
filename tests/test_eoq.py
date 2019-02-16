import pytest
from eoq import EOQ
from demand import Demand
from rawcosts import RawCosts


# -- Q* (optimal order quantity) --

def test_optimal_order_quantity_with_missing_raw_scores_raises():
    with pytest.raises(ValueError):
        EOQ.optimal_order_quantity(raw_costs=None, demand=get_demand())


def test_optimal_order_quantity_with_missing_demand_raises():
    with pytest.raises(ValueError):
        EOQ.optimal_order_quantity(raw_costs=get_raw_costs(), demand=None)


def test_optimal_order_quantity_calculates_correctly():
    import math
    demand = get_demand()
    raw_costs = get_raw_costs()

    q_star = EOQ.optimal_order_quantity(raw_costs=raw_costs, demand=demand)

    assert q_star == math.sqrt(
        2 * (raw_costs.ordering_cost * demand.quantity) /
        raw_costs.holding_cost
    )


def test_optimal_order_quantity_with_zero_holding_cost_returns_demand():
    demand = get_demand()
    raw_costs = get_raw_costs(holding_rate=0.0)

    q_star = EOQ.optimal_order_quantity(raw_costs=raw_costs, demand=demand)

    assert q_star == demand.quantity


# -- T* (optimal cycle time) --

def test_optimal_cycle_time_with_missing_raw_scores_raises():
    with pytest.raises(ValueError):
        EOQ.optimal_cycle_time(raw_costs=None, demand=get_demand())


def test_optimal_cycle_time_with_holding_cost_zero_raises():
    with pytest.raises(ValueError):
        EOQ.optimal_cycle_time(raw_costs=get_raw_costs(holding_rate=0.0), demand=get_demand())


def test_optimal_cycle_time_with_missing_demand_raises():
    with pytest.raises(ValueError):
        EOQ.optimal_cycle_time(raw_costs=get_raw_costs(), demand=None)


def test_optimal_cycle_time_with_demand_zero_raises():
    with pytest.raises(ValueError):
        EOQ.optimal_cycle_time(raw_costs=get_raw_costs(), demand=get_demand(quantity=0))


def test_optimal_cycle_time_calculates_correctly():
    import math
    demand = get_demand()
    raw_costs = get_raw_costs()

    t_star = EOQ.optimal_cycle_time(raw_costs=raw_costs, demand=demand)

    assert t_star == math.sqrt(
        (2 * raw_costs.ordering_cost) /
        (demand.quantity * raw_costs.holding_cost)
    )


# -- TRC(Q*)  (optimal relevant cost) --

def test_optimal_relevant_cost_with_missing_raw_costs_raises():
    with pytest.raises(ValueError):
        EOQ.optimal_relevant_cost(raw_costs=None, demand=get_demand())


def test_optimal_relevant_cost_with_missing_demand_raises():
    with pytest.raises(ValueError):
        EOQ.optimal_relevant_cost(raw_costs=get_raw_costs(), demand=None)


def test_optimal_relevant_cost_calculates_correctly():
    import math
    raw_costs = get_raw_costs()
    demand = get_demand()

    expected = math.sqrt(2 *
                         raw_costs.ordering_cost *
                         raw_costs.holding_cost *
                         demand.quantity)
    actual = EOQ.optimal_relevant_cost(raw_costs=raw_costs, demand=demand)

    assert expected == actual


# -- TC(Q*)  (optimal total cost) --

def test_optimal_total_cost_with_missing_raw_costs_raises():
    with pytest.raises(ValueError):
        EOQ.optimal_total_cost(raw_costs=None, demand=get_demand())


def test_optimal_total_cost_with_missing_demand_raises():
    with pytest.raises(ValueError):
        EOQ.optimal_total_cost(raw_costs=get_raw_costs(), demand=None)


def test_optimal_total_cost_calculates_correctly():
    raw_costs = get_raw_costs()
    demand = get_demand()

    trc = EOQ.optimal_relevant_cost(raw_costs, demand)
    expected = trc + raw_costs.unit_cost * demand.quantity

    actual = EOQ.optimal_total_cost(raw_costs=raw_costs, demand=demand)

    assert expected == actual


# -- HELPER METHODS --

def get_demand(quantity=1000):
    return Demand(quantity)


def get_raw_costs(holding_rate=0.25):
    return RawCosts(unit_cost=1.00, ordering_cost=25.00, holding_rate=holding_rate)
