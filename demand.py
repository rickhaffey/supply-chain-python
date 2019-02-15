from validation import Validate


class Demand:
    """
    Captures all demand-related values.

    Parameters
    ----------
    quantity : int
        The amount of demand, in units
    time_unit : {{'Y', 'M', 'W', 'D'}}, default 'Y'
        A time unit specifier, representing the period of time over which the `quantity` applies
    """

    def __init__(self, quantity, time_unit='Y'):
        Validate.required(quantity, "quantity")
        Validate.non_negative(quantity, "quantity")
        self.quantity = quantity

        Validate.one_of_allowable(time_unit, ['Y', 'M', 'W', 'D'], "time_unit")
        self.time_unit = time_unit
