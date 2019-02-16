from validation import Validate
import math


class EOQ:

    @staticmethod
    def optimal_order_quantity(raw_costs, demand):
        """
        Calculate economic order quantity (optimal Q*) given raw costs and demand.

        Parameters
        ----------
        raw_costs : RawCosts
            A `RawCosts` object, containing a set of raw cost values
        demand : Demand
            A `Demand` object, containing demand quantity and time frame

        Returns
        -------
        optimal_order_quantity: float
        """

        Validate.required(raw_costs, "raw_costs")
        Validate.required(demand, "demand")

        # if holding cost is 0, optimal Q would be D (i.e.
        # minimize ordering cost with one order across all demand)
        if raw_costs.holding_cost == 0.0:
            return demand.quantity
        else:
            numerator = 2 * raw_costs.ordering_cost * demand.quantity
            denominator = raw_costs.holding_cost

            return math.sqrt(numerator / denominator)

    @staticmethod
    def optimal_cycle_time(raw_costs, demand):
        """
        Calculate optimal cycle time (T*) given raw costs and demand.

        Parameters
        ----------
        raw_costs : RawCosts
            A `RawCosts` object, containing a set of raw cost values
        demand : Demand
            A `Demand` object, containing demand quantity and time frame

        Returns
        -------
        optimal_cycle_time: float
        """

        Validate.required(raw_costs, "raw_costs")
        Validate.required(demand, "demand")
        Validate.positive(demand.quantity, "demand.quantity")
        Validate.positive(raw_costs.holding_cost, "raw_costs.holding_cost")

        numerator = 2 * raw_costs.ordering_cost
        denominator = demand.quantity * raw_costs.holding_cost

        return math.sqrt(numerator / denominator)

    @staticmethod
    def optimal_relevant_cost(raw_costs, demand):
        """
        Calculate optimal relevant cost. (TRC(Q*))

        Parameters
        ----------
        raw_costs : RawCosts
            A `RawCosts` object, containing a set of raw cost values
        demand : Demand
            A `Demand` object, containing demand quantity and time frame

        Returns
        -------
        optimal_relevant_cost: float
        """

        Validate.required(raw_costs, "raw_costs")
        Validate.required(demand, "demand")

        return math.sqrt(2 *
                         raw_costs.ordering_cost *
                         raw_costs.holding_cost *
                         demand.quantity)

    @staticmethod
    def optimal_total_cost(raw_costs, demand):
        """
        Calculate optimal total cost. (TC(Q*))

        Parameters
        ----------
        raw_costs : RawCosts
            A `RawCosts` object, containing a set of raw cost values
        demand : Demand
            A `Demand` object, containing demand quantity and time frame

        Returns
        -------
        optimal_total_cost: float
        """

        Validate.required(raw_costs, "raw_costs")
        Validate.required(demand, "demand")

        return (raw_costs.unit_cost * demand.quantity +
                EOQ.optimal_relevant_cost(raw_costs=raw_costs, demand=demand))
