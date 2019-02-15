from validation import Validate


class RawCosts:
    """
    Captures all inventory-related "raw" costs.  Typically used for calculating
    economic order quantity, total cost, total relevant cost, etc.

    Parameters
    ----------
    unit_cost : float
        Cost per unit, in dollars
    ordering_cost : float
        Cost per order, in dollars
    holding_rate : float
        Cost per dollar of inventory per `holding_time_unit`, as a percentage.  Used to calculate
        `holding_cost` as `unit_cost` times `holding_rate`
    holding_cost : float
        Carrying / Holding cost per unit over a period of time (specified by `holding_time_unit`),
        in dollars
    holding_time_unit : {{'Y', 'M', 'W', 'D'}}, default 'Y'
        A time unit specifier, representing the period of time over which the `holding_rate` /
        `holding_cost` applies
    shortage_cost : int or float, optional, default 0
        Cost per unit short, in dollars
    """

    supported_time_units = ['Y', 'M', 'W', 'D']

    def __init__(self, unit_cost, ordering_cost, holding_rate=None,
                 holding_cost=None, holding_time_unit='Y',
                 shortage_cost=0):
        RawCosts.validate_init_values(unit_cost, ordering_cost, holding_rate,
                                      holding_cost, holding_time_unit,
                                      shortage_cost)
        self.unit_cost = unit_cost
        self.ordering_cost = ordering_cost

        # calculate holding cost from holding rate
        # (and vice-versa), depending on which is provided
        if holding_rate is not None:
            self.holding_rate = holding_rate
            self.holding_cost = holding_rate * self.unit_cost
        else:
            self.holding_cost = holding_cost
            self.holding_rate = holding_cost / self.unit_cost

        self.holding_time_unit = holding_time_unit
        self.shortage_cost = shortage_cost

    @staticmethod
    def validate_init_values(unit_cost, ordering_cost, holding_rate,
                             holding_cost, holding_time_unit,
                             shortage_cost):
        Validate.required(unit_cost, "unit_cost")
        Validate.non_negative(unit_cost, "unit_cost")

        Validate.required(ordering_cost, "ordering_cost")
        Validate.non_negative(ordering_cost, "ordering_cost")

        # accept holding_rate or holding_cost, but not both
        # (at least one is required)
        Validate.one_only([holding_rate, holding_cost], ["holding_rate", "holding_cost"])
        if holding_rate is not None:
            Validate.non_negative(holding_rate, "holding_rate")
        else:
            Validate.non_negative(holding_cost, holding_cost)

        Validate.one_of_allowable(holding_time_unit, RawCosts.supported_time_units,
                                  "holding_time_unit")

        Validate.required(shortage_cost, "shortage_cost")
        Validate.non_negative(shortage_cost, "shortage_cost")
