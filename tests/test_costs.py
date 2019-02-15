import pytest
from costs import Costs
from demand import Demand
from rawcosts import RawCosts


# -- PURCHASE COST --

def test_purchase_cost_with_missing_unit_cost_raises():
    with pytest.raises(ValueError):
        Costs.purchase_cost(unit_cost=None, demand_quantity=1)


def test_purchase_cost_with_negative_unit_cost_raises():
    with pytest.raises(ValueError):
        Costs.purchase_cost(unit_cost=-1.0, demand_quantity=1)


def test_purchase_cost_with_missing_demand_quantity_raises():
    with pytest.raises(ValueError):
        Costs.purchase_cost(unit_cost=1.0, demand_quantity=None)


def test_purchase_cost_with_negative_demand_quantity_raises():
    with pytest.raises(ValueError):
        Costs.purchase_cost(unit_cost=1.0, demand_quantity=-1)


def test_purchase_cost_calculates_result():
    pc = Costs.purchase_cost(unit_cost=1.25, demand_quantity=25)
    assert pc == 1.25 * 25


# -- ORDERING COST --

def test_ordering_cost_with_missing_ordering_cost_raises():
    with pytest.raises(ValueError):
        Costs.ordering_cost(ordering_cost=None, demand_quantity=1, order_quantity=1)


def test_ordering_cost_with_negative_ordering_cost_raises():
    with pytest.raises(ValueError):
        Costs.ordering_cost(ordering_cost=-1.0, demand_quantity=1, order_quantity=1)


def test_ordering_cost_with_missing_demand_quantity_raises():
    with pytest.raises(ValueError):
        Costs.ordering_cost(ordering_cost=1.0, demand_quantity=None, order_quantity=1)


def test_ordering_cost_with_negative_demand_quantity_raises():
    with pytest.raises(ValueError):
        Costs.ordering_cost(ordering_cost=1.0, demand_quantity=-1, order_quantity=1)


def test_ordering_cost_with_missing_order_quantity_raises():
    with pytest.raises(ValueError):
        Costs.ordering_cost(ordering_cost=1.0, demand_quantity=1, order_quantity=None)


def test_ordering_cost_with_negative_order_quantity_raises():
    with pytest.raises(ValueError):
        Costs.ordering_cost(ordering_cost=1.0, demand_quantity=1, order_quantity=-1)


def test_ordering_cost_with_zero_order_quantity_raises():
    with pytest.raises(ValueError):
        Costs.ordering_cost(ordering_cost=1.0, demand_quantity=1, order_quantity=0)


def test_ordering_cost_calculates_correctly():
    oc = Costs.ordering_cost(ordering_cost=100.0, demand_quantity=250, order_quantity=25)
    assert oc == 100.0 * (250 / 25)


# -- HOLDING COST --

def test_holding_cost_with_missing_holding_cost_raises():
    with pytest.raises(ValueError):
        Costs.holding_cost(holding_cost=None, order_quantity=1)


def test_holding_cost_with_negative_holding_cost_raises():
    with pytest.raises(ValueError):
        Costs.holding_cost(holding_cost=-1.0, order_quantity=1)


def test_holding_cost_with_missing_order_quantity_raises():
    with pytest.raises(ValueError):
        Costs.holding_cost(holding_cost=1.0, order_quantity=None)


def test_holding_cost_with_negative_order_quantity_raises():
    with pytest.raises(ValueError):
        Costs.holding_cost(holding_cost=1.0, order_quantity=-1)


def test_holding_cost_calculates_correctly():
    hc = Costs.holding_cost(holding_cost=0.25, order_quantity=100)
    assert hc == 0.25 * (100 / 2)


# -- SHORTAGE COST --

def test_shortage_cost_with_missing_shortage_cost_raises():
    with pytest.raises(ValueError):
        Costs.shortage_cost(shortage_cost=None, shortage_quantity=1)


def test_shortage_cost_with_negative_shortage_cost_raises():
    with pytest.raises(ValueError):
        Costs.shortage_cost(shortage_cost=-1.0, shortage_quantity=1)


def test_shortage_cost_with_missing_shortage_quantity_raises():
    with pytest.raises(ValueError):
        Costs.shortage_cost(shortage_cost=1.0, shortage_quantity=None)


def test_shortage_cost_with_negative_shortage_quantity_raises():
    with pytest.raises(ValueError):
        Costs.shortage_cost(shortage_cost=1.0, shortage_quantity=-1)


def test_shortage_cost_calculates_correctly():
    sc = Costs.shortage_cost(shortage_cost=2.00, shortage_quantity=125)
    assert sc == 2.00 * 125


# -- TOTAL RELEVANT COST --

def test_trc_with_missing_raw_costs_raises():
    with pytest.raises(ValueError):
        Costs.total_relevant_cost(raw_costs=None, demand=get_demand(), order_quantity=100)


def test_trc_with_missing_demand_raises():
    with pytest.raises(ValueError):
        Costs.total_relevant_cost(raw_costs=get_raw_costs(), demand=None, order_quantity=100)


def test_trc_with_missing_order_quantity_raises():
    with pytest.raises(ValueError):
        Costs.total_relevant_cost(raw_costs=get_raw_costs(),
                                  demand=get_demand(),
                                  order_quantity=None)


def test_trc_calculates_correctly():
    # arrange
    demand = get_demand()
    raw_costs = get_raw_costs()
    order_quantity = 100

    # act
    trc = Costs.total_relevant_cost(raw_costs=raw_costs,
                                    demand=demand,
                                    order_quantity=order_quantity)

    # assert
    ordering_cost = Costs.ordering_cost(ordering_cost=raw_costs.ordering_cost,
                                        demand_quantity=demand.quantity,
                                        order_quantity=order_quantity)
    holding_cost = Costs.holding_cost(holding_cost=raw_costs.holding_cost,
                                      order_quantity=order_quantity)

    assert trc == ordering_cost + holding_cost


# -- TOTAL COST --

def test_tc_with_missing_raw_costs_raises():
    with pytest.raises(ValueError):
        Costs.total_cost(raw_costs=None, demand=get_demand(), order_quantity=100)


def test_tc_with_missing_demand_raises():
    with pytest.raises(ValueError):
        Costs.total_cost(raw_costs=get_raw_costs(), demand=None, order_quantity=100)


def test_tc_with_missing_order_quantity_raises():
    with pytest.raises(ValueError):
        Costs.total_cost(raw_costs=get_raw_costs(), demand=get_demand(), order_quantity=None)


def test_tc_with_missing_expected_shortage_raises():
    with pytest.raises(ValueError):
        Costs.total_cost(raw_costs=get_raw_costs(),
                         demand=get_demand(),
                         order_quantity=100,
                         expected_shortage=None)


def test_tc_calculates_correctly():
    # arrange
    demand = get_demand()
    raw_costs = get_raw_costs()
    order_quantity = 100

    # act
    tc = Costs.total_cost(raw_costs=raw_costs, demand=demand, order_quantity=order_quantity)

    # assert
    purchase_cost = Costs.purchase_cost(unit_cost=raw_costs.unit_cost,
                                        demand_quantity=demand.quantity)
    shortage_cost = Costs.shortage_cost(shortage_cost=raw_costs.shortage_cost,
                                        shortage_quantity=0)
    trc = Costs.total_relevant_cost(raw_costs=raw_costs,
                                    demand=demand,
                                    order_quantity=order_quantity)

    assert tc == purchase_cost + trc + shortage_cost


# -- HELPER METHODS --

def get_demand():
    return Demand(1000)


def get_raw_costs():
    return RawCosts(unit_cost=1.00, ordering_cost=25.00, holding_rate=0.25)
