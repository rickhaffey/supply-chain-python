import pytest
from rawcosts import RawCosts


def test_init_with_missing_unit_cost_raises():
    with pytest.raises(ValueError):
        RawCosts(unit_cost=None, ordering_cost=1.0, holding_cost=1.0)


def test_init_with_negative_unit_cost_raises():
    with pytest.raises(ValueError):
        RawCosts(unit_cost=-1.0, ordering_cost=1.0, holding_cost=1.0)


def test_init_with_positive_unit_cost_captures():
    rc = RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_cost=1.0)
    assert rc.unit_cost == 1.0


def test_init_with_missing_ordering_cost_raises():
    with pytest.raises(ValueError):
        RawCosts(unit_cost=1.0, ordering_cost=None, holding_cost=1.0)


def test_init_with_negative_ordering_cost_raises():
    with pytest.raises(ValueError):
        RawCosts(unit_cost=1.0, ordering_cost=-1.0, holding_cost=1.0)


def test_init_with_positive_ordering_cost_captures():
    rc = RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_cost=1.0)
    assert rc.ordering_cost == 1.0


def test_init_with_none_shortage_cost_raises():
    with pytest.raises(ValueError):
        RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_cost=1.0, shortage_cost=None)


def test_init_with_negative_shortage_cost_raises():
    with pytest.raises(ValueError):
        RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_cost=1.0, shortage_cost=-1.0)


def test_init_with_positive_shortage_cost_captures():
    rc = RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_cost=1.0, shortage_cost=1.0)
    assert rc.shortage_cost == 1.0


def test_init_with_missing_shortage_cost_captures_zero_default():
    rc = RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_cost=1.0)
    assert rc.shortage_cost == 0.0


def test_init_with_missing_holding_rate_and_cost_raises():
    with pytest.raises(ValueError):
        RawCosts(unit_cost=1.0, ordering_cost=1.0)


def test_init_with_holding_rate_and_cost_raises():
    with pytest.raises(ValueError):
        RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_rate=0.25, holding_cost=1.0)


def test_init_with_negative_holding_rate_raises():
    with pytest.raises(ValueError):
        RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_rate=-0.25)


def test_init_with_zero_holding_rate_captures():
    rc = RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_rate=0.0)
    assert rc.holding_rate == 0.0
    assert rc.holding_cost == 0.0


def test_init_with_negative_holding_cost_raises():
    with pytest.raises(ValueError):
        RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_cost=-1.0)


def test_init_with_positive_holding_rate_captures():
    rc = RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_rate=0.25)
    assert rc.holding_rate == 0.25


def test_init_with_positive_holding_cost_captures():
    rc = RawCosts(unit_cost=1.0, ordering_cost=1.0, holding_cost=1.0)
    assert rc.holding_cost == 1.0


def test_init_with_holding_cost_calcs_holding_rate():
    rc = RawCosts(unit_cost=10.0, ordering_cost=1.0, holding_cost=2.50)
    assert rc.holding_rate == 0.25


def test_init_with_holding_rate_calcs_holding_cost():
    rc = RawCosts(unit_cost=10.0, ordering_cost=1.0, holding_rate=0.25)
    assert rc.holding_cost == 2.50
