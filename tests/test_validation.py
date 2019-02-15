import pytest
from validation import Validate


def test_required_with_none_raises():
    with pytest.raises(ValueError):
        Validate.required(None, "test_value")


def test_required_with_some_passes():
    Validate.required("not None", "test_value")


def test_non_negative_with_positive_passes():
    Validate.non_negative(1, "test_value")


def test_non_negative_with_zero_passes():
    Validate.non_negative(0, "test_value")


def test_non_negative_with_negative_fails():
    with pytest.raises(ValueError):
        Validate.non_negative(-1, "test_value")


def test_positive_with_positive_passes():
    Validate.positive(1, "test_value")


def test_positive_with_zero_fails():
    with pytest.raises(ValueError):
        Validate.positive(0, "test_value")


def test_positive_with_negative_fails():
    with pytest.raises(ValueError):
        Validate.positive(-1, "test_value")


def test_one_only_with_one_only_passes():
    values = [None, 2, None]
    names = ["one", "two", "three"]
    Validate.one_only(values, names)


def test_one_only_with_more_than_one_fails():
    values = [None, 2, 3]
    names = ["one", "two", "three"]
    with pytest.raises(ValueError):
        Validate.one_only(values, names)


def test_one_only_with_less_than_one_fails():
    values = [None, None, None]
    names = ["one", "two", "three"]
    with pytest.raises(ValueError):
        Validate.one_only(values, names)


def test_one_of_allowable_with_allowable_passes():
    Validate.one_of_allowable("YES", ["YES", "NO"], "test_value")


def test_one_of_allowable_with_other_fails():
    with pytest.raises(ValueError):
        Validate.one_of_allowable("MAYBE", ["YES", "NO"], "test_value")
