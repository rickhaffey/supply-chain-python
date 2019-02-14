import validation as v


class RawCosts:
    """
    Captures all inventory-related "raw" costs.  Typically used for calculating
    economic order quantity, total cost, total relevant cost, etc.

    Parameters
    ----------
    unit_cost : int or float
        Cost per unit, in dollars
    ordering_cost : int or float
        Cost per order, in dollars
    holding_rate : float
        Cost per dollar of inventory per `holding_time_unit`, as a percentage.  Used to calculate
        `holding_charge` as `unit_cost` times `holding_rate`
    holding_charge : float
        Carrying / Holding cost per unit over a period of time (specified by `holding_time_unit`), in dollars
    holding_time_unit : {{'Y', 'M', 'W', 'D'}}, default 'Y'
        A time unit specifier, representing the period of time over which the `holding_rate` /
        `holding_charge` applies
    """

    def __init__(self, unit_cost, ordering_cost, holding_rate=None, holding_charge=None, holding_time_unit='Y'):
        v.validate_required(unit_cost, "unit_cost")
        v.validate_non_negative(unit_cost, "unit_cost")
        self.unit_cost = unit_cost

        v.validate_required(ordering_cost, "ordering_cost")
        v.validate_non_negative(ordering_cost, "ordering_cost")
        self.ordering_cost = ordering_cost

        # accept holding_rate or holding_charge, but not both
        # (at least one is required)
        v.validate_one_only([holding_rate, holding_charge], ["holding_rate", "holding_charge"])
        if holding_rate:
            self.holding_rate = holding_rate
            self.holding_charge = holding_rate / self.unit_cost
        else:
            self.holding_charge = holding_charge
            self.holding_rate = holding_charge * self.unit_cost

        v.validate_one_of_allowable(holding_time_unit, ['Y', 'M', 'W', 'D'], "holding_time_unit")
        self.holding_time_unit = holding_time_unit
