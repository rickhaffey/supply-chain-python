import pytest
from demand import Demand


def test_init_with_missing_quantity_raises():
    with pytest.raises(ValueError):
        Demand(quantity=None)


def test_init_with_negative_quantity_raises():
    with pytest.raises(ValueError):
        Demand(quantity=-1)


def test_init_with_positive_quantity_captures():
    d = Demand(quantity=1)
    assert d.quantity == 1


def test_init_with_valid_time_unit_captures():
    d = Demand(quantity=1, time_unit='W')
    assert d.time_unit == 'W'


def test_init_with_invalid_time_unit_raises():
    with pytest.raises(ValueError):
        Demand(quantity=1, time_unit='X')
