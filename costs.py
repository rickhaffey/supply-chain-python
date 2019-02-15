from validation import Validate


class Costs:
    """
    Provides methods for calculating costs, both at the "detail" level (e.g.
    purchase cost, ordering cost, etc.) and at the "combined" level (i.e.
    total relevant cost (TRC) and total cost (TC).
    """

    @staticmethod
    def purchase_cost(unit_cost, demand_quantity):
        """
        Calculate the purchase cost - the total landed cost for acquiring
        product needed to satisfy a given amount of demand.

        Parameters
        ----------
        unit_cost : int or float
            Cost per unit, in dollars
        demand_quantity : int
            The amount of demand, in units

        Returns
        -------
        purchase_cost: float
        """

        Validate.required(unit_cost, "unit_cost")
        Validate.non_negative(unit_cost, "unit_cost")

        Validate.required(demand_quantity, "demand_quantity")
        Validate.non_negative(demand_quantity, "demand_quantity")

        return unit_cost * demand_quantity

    @staticmethod
    def ordering_cost(ordering_cost, demand_quantity, order_quantity):
        """
        Calculate the ordering cost - the total cost of placing, receiving,
        and processing orders needed to fulfill a given amount of demand.

        Parameters
        ----------
        ordering_cost : int or float
            Cost per order, in dollars
        demand_quantity : int
            The amount of demand, in units
        order_quantity : int
            The number of units purchased per order, in units

        Returns
        -------
        ordering_cost: float
        """

        Validate.required(ordering_cost, "ordering_cost")
        Validate.non_negative(ordering_cost, "ordering_cost")

        Validate.required(demand_quantity, "demand_quantity")
        Validate.non_negative(demand_quantity, "demand_quantity")

        Validate.required(order_quantity, "order_quantity")
        Validate.positive(order_quantity, "order_quantity")

        return ordering_cost * (demand_quantity / order_quantity)

    @staticmethod
    def holding_cost(holding_cost, order_quantity):
        """
        Calculate the holding cost - the total cost of holding excess inventory,
        including storage, service costs, risk costs, and capital costs.

        Parameters
        ----------
        holding_cost : int or float
            Cost per unit of inventory per time period, in dollars
        order_quantity : int
            The number of units purchased per order, in units

        Returns
        -------
        holding_cost: float
        """

        Validate.required(holding_cost, "holding_cost")
        Validate.non_negative(holding_cost, "holding_cost")

        Validate.required(order_quantity, "order_quantity")
        Validate.non_negative(order_quantity, "order_quantity")

        return holding_cost * (order_quantity / 2)

    @staticmethod
    def shortage_cost(shortage_cost, shortage_quantity):
        """
        Calculate the shortage cost - the total cost of not having units in stock,
        including costs due to backorder, lost sales, lost customers, and operational
        disruptions.

        Parameters
        ----------
        shortage_cost : int or float
            Cost per unit of shortage, in dollars
        shortage_quantity : int
            The number of units of shortage, in units

        Returns
        -------
        shortage_cost : float
        """

        Validate.required(shortage_cost, "shortage_cost")
        Validate.non_negative(shortage_cost, "shortage_cost")

        Validate.required(shortage_quantity, "shortage_quantity")
        Validate.non_negative(shortage_quantity, "shortage_quantity")

        return shortage_cost * shortage_quantity

    @staticmethod
    def total_cost(raw_costs, demand, order_quantity, expected_shortage=0):
        """
        Calculate total inventory cost - the combination of purchase,
        ordering, holding, and shortage cost components.

        Parameters
        ----------
        raw_costs : RawCosts
            A `RawCosts` object, containing a set of raw cost values
        demand : Demand
            A `Demand` object, containing demand quantity and time frame
        order_quantity : int
            The number of units purchased with each order
        expected_shortage : int, default 0
            The expected value of the number of units short

        Returns
        -------
        total_cost : float
        """

        Validate.required(raw_costs, "raw_costs")
        Validate.required(demand, "demand")
        Validate.required(order_quantity, "order_quantity")
        Validate.required(expected_shortage, "expected_shortage")

        return (Costs.purchase_cost(raw_costs.unit_cost, demand.quantity) +
                Costs.total_relevant_cost(raw_costs, demand, order_quantity) +
                Costs.shortage_cost(raw_costs.shortage_cost, expected_shortage))

    @staticmethod
    def total_relevant_cost(raw_costs, demand, order_quantity):
        """
        Calculate total inventory cost relevant to the calculation of economic order
        quantity.

        Note: The relevant cost components are those that change as a function of
        order quantity: ordering cost and holding cost.

        Parameters
        ----------
        raw_costs : RawCosts
            A `RawCosts` object, containing a set of raw cost values
        demand : Demand
            A `Demand` object, containing demand order_quantity and time frame
        order_quantity : int
            The number of units purchased with each order

        Returns
        -------
        total_relevant_cost : float
        """

        Validate.required(raw_costs, "raw_costs")
        Validate.required(demand, "demand")
        Validate.required(order_quantity, "order_quantity")

        return (Costs.ordering_cost(raw_costs.ordering_cost, demand.quantity, order_quantity) +
                Costs.holding_cost(raw_costs.holding_cost, order_quantity))
