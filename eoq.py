# W04-L02-QQ02

from math import sqrt, ceil
# from __future__ import division


class EOQ:
    """
    Economic Order Quantity calculations.
    Provides the ability to calculate optimal order quantity (Q*), and by extension,
    optimal order cycle time (T*), optimal total relevant costs (TRC*) and total costs
    (TC*).  Also provides the ability to convert between time units and unit multiples.
    Supports sensitivity analysis by comparing optimal costs against costs resulting from
    changes in order quantity, demand, and cycle time.
    Generates summary metrics, and allows producing explanatory metrics and plots.

    Parameters
    ----------
    demand : Average total annual demand, in units / year
    ordering_cost : Fixed ordering cost, in $ / order
    unit_cost : Variable (Purchase) cost, in $ / unit
    holding_charge : Carrying or Holding charge, in $ / inventory or $ / time
     """
    def __init__(self, demand, ordering_cost, unit_cost, holding_charge):
        # TODO: default time_units="Y", allow providing others (W, D, Q?)
        assert(demand > 0)
        assert(ordering_cost > 0)
        assert(unit_cost > 0)
        assert(holding_charge > 0)

        self.demand = demand
        self.ordering_cost = ordering_cost
        self.unit_cost = unit_cost
        self.holding_charge = holding_charge
        self.q_star = self.__q_star()
        self.t_star = self.__t_star()

    def __q_star(self):
        numerator = 2 * self.ordering_cost * self.demand
        denominator = self.__holding_cost()

        assert(denominator != 0)

        q_star = sqrt(numerator / denominator)

        return q_star

    def __t_star(self):
        return self.q_star / self.demand

    def total_relevant_cost(self, q=None):
        if q is None:
            q = self.q_star

        return (self.ordering_cost * (self.demand / q) +
                self.__holding_cost() * (q / 2))

    def total_cost(self, unit_shortage_cost=0, expected_shortage=0):
        return (self.unit_cost * self.demand +
                self.total_relevant_cost() +
                unit_shortage_cost * expected_shortage)

    def __holding_cost(self):
        return self.unit_cost * self.holding_charge

    def power_of_two_policies(self):
        from math import log
        # NOTE: in weekly time units
        t_weekly = self.__t_star() * 52
        lower = t_weekly / sqrt(2)
        upper = t_weekly * sqrt(2)
        k = ceil(log(lower, 2))
        return lower, 2 ** k, upper

    def convert(self, time_units='Y', multiples=1):
        # TODO convert from current to provided time units and multiples,
        # returning a new EOW instance
        pass

    def summary(self):
        print("*** EOQ ***")
        print("Q*: {}".format(self.q_star))
        print("\t(rounded: {})".format(ceil(self.q_star)))
        print(f"\tcost: ${self.q_star * self.unit_cost}")
        print('\t(rounded cost: ${})'.format(ceil(self.q_star * self.unit_cost)))
        print(f'T*: {self.t_star}')
        print("\tmonths of supply: {}".format(self.t_star * 12))
        print("\tweeks of supply: {}".format(self.t_star * 52))
        print("\tdays of supply: {}".format(self.t_star * 365))



from pytest import approx

def test_q_star():
    demand = 1200
    ordering_cost = 100
    unit_cost = 10
    holding_charge = 0.10

    eoq = EOQ(demand=demand,
              ordering_cost=ordering_cost,
              unit_cost=unit_cost,
              holding_charge=holding_charge)

    assert(489.898 == approx(eoq.q_star, 0.001))


def test_t_star():
    demand = 1200
    ordering_cost = 100
    unit_cost = 10
    holding_charge = 0.10

    eoq = EOQ(demand=demand,
              ordering_cost=ordering_cost,
              unit_cost=unit_cost,
              holding_charge=holding_charge)

    assert(0.4082 == approx(eoq.t_star, 0.001))


def qq_s():
    # Finding Economic Order Quantity

    # Suppose you have a product with very stable demand of 1,200 units per year.
    # The ordering cost is $100 per order, the cost of the item is $10 per unit,
    # and the cost of carrying inventory is 10% per annum.  You sell this product
    # to your customers for $17.50 per unit.

    demand = 1200
    ordering_cost = 100
    unit_cost = 10
    holding_charge = 0.10

    # Part 1
    # What is the economic order quantity (EOQ) or Q* in units? Round up to the nearest integer value.


    eoq = EOQ(demand=demand,
              ordering_cost=ordering_cost,
              unit_cost=unit_cost,
              holding_charge=holding_charge)

    print("Q*: {}".format(ceil(eoq.q_star)))

    # Part 2
    # What is the value of Q* in dollars? Round up to the nearest integer dollar value and do not enter a dollar sign.

    q_star_cost = ceil(eoq.q_star * unit_cost)
    print("Q* $: {}".format(q_star_cost))

    # Part 3
    # Sometimes, the amount of inventory is described in terms of how long it would last with the existing demand,
    # e.g., weeks of supply or months of supply. What is Q* in terms of Months of Supply?
    # Enter your answer with two significant digits.

    months_of_supply = eoq.t_star * 12
    print("MOS: {}".format(months_of_supply))


    # Part 4
    # What is the optimal order cycle time in days? Answer to the nearest integer value.
    t_star_days = round(eoq.t_star * 365)
    print("T* (days): {}".format(t_star_days))

    # Part 5
    # Suppose that the shipment pallets are sized such that the orders have to be in multiples of 50 units.
    # What is the new EOQ in Units?

    pallet_size = 50
    pallets = ceil(eoq.q_star / 50)
    new_EOQ = pallets * pallet_size
    print("New Q*: {}".format(new_EOQ))


    eoq.summary()


# W04-L02-QQ03

# Part 1
# You are the inventory control manager for a large firm. At the annual planning session,
# you are setting the inventory policy for your major items. While doing this, you realize that
# it is difficult to accurately estimate the actual cost for placing an order. Therefore, to be
# on the safer side, you decide to set the actual order quantity at 25% more than the computed economic order quantity.

# By how much (in percentage) will the new Total Relevant Cost be different from the optimal TRC*?
# Enter your answer as a decimal between 0 and 1 with 3 significant digits. For example, for 32.12% enter 0.321.

# Part 2
# You realize that the actual demand is 25% MORE than forecasted demand. By what percentage will the new
# TRC be different from the optimal TRC*? Enter your answer as a decimal between zero and one, e.g.,
# for 32.12% enter 0.3212.

# Part 3
# Suppose now you realize that the actual demand is 25% LESS than forecasted demand. By what percentage
# will the new TRC be different from the optimal TRC*? Enter your answer as a decimal between zero and one,
# e.g., for 32.12% enter 0.3212.


# W04-L02-QQ04

# You are managing the inventory for an item valued at $100 per unit.  It costs about $300 to place an order due to
# employee salaries and the system costs.   The annual demand is 27,500 units per year and you have a holding cost
# rate is 24% per year.

# Part 2a
# What is the economic order quantity Q* in units for this item? Round up to the next highest integer value.

# Part 2b What is the optimal order cycle time T* in weeks for this item? Assume 52 weeks in the year and use three
# significant digits, that is, if your answer is 3.4567, enter 3.46.

# Part 2c You have decided that it makes no sense to place an order at the frequency. Suppose you want to place an
# order every Monday morning. What would your order quantity be each week assuming a 52 week year? Round up to the
# nearest integer value.

# Part 2d How much more is your new policy of ordering once a week going to cost you in dollars per year as compared
# to the optimal order frequency? Round up to the next highest integer value, and use the solutions to previous
# problems for values of Q and Q*.

# Part 2e
# You want to continue to order on only Mondays. However, you are considering ordering on periodic Mondays.
#
# Which of the following ordering policies would produce the lowest total relevant cost?

def w04_00_basic_eoq():
    # W04-PP-Basic EOQ
    print('\n# W04-PP-Basic EOQ #\n')
    demand = 4600  # units / yr
    ordering_cost = 250  # $ / order
    holding_charge = 0.25  # % of inventory $ / year
    unit_cost = 12  # $ / unit

    eoq = EOQ(demand=demand, ordering_cost=ordering_cost, holding_charge=holding_charge, unit_cost=unit_cost)
    print(ceil(eoq.q_star))

    print(eoq.power_of_two_policies())


def w04_pp_partial_foods():
    # W04-PP-Partial Foods
    print('\n# W04-PP-Partial Foods\n')

    # You are responsible for managing the inventory for the trendy upscale specialty food store, Partial Foods.
    # You are trying to set the inventory policy for one of your most popular cheeses, Mad Cow Cheddar,
    # which comes in 1 pound wheels.   It is a stable selling cheese with an average weekly demand of 14 wheels/week.
    demand_weekly = 14  # wheels / week
    demand = demand_weekly * 52

    # Your fixed cost of placing an order from the farm that produces Mad Cow Cheddar is $90/order and the cheese itself
    # costs you $12.50 per wheel.   Assume that there are 52 weeks in a year and that the annual inventory holding
    # charge is 20%.
    ordering_cost = 90  # $ / order
    unit_cost = 12.50  # $ / unit
    holding_charge = 0.20  # % of $ inv / year

    eoq = EOQ(demand=demand, ordering_cost=ordering_cost, holding_charge=holding_charge, unit_cost=unit_cost)
    print(ceil(eoq.q_star))

    t_star_weekly = eoq.t_star * 52
    avg_weeks_on_shelf = t_star_weekly / 2
    print(round(avg_weeks_on_shelf))

    shelf_cost = 10  # $ / sq-ft week
    space_per_unit = 0.15  # sq-ft

    shelf_cost_per_unit = shelf_cost * space_per_unit * 52  # annual shelf cost per unit
    q_star = sqrt((2 * ordering_cost * demand) / (holding_charge * unit_cost + shelf_cost_per_unit))
    print(q_star)

    print(3 / space_per_unit)


def w04_pp_part4():
    # TODO - PP 4 - questions around adjusting demand, and impact on Q* or TRC*
    pass


def w04_pp_incremental_discounts():
    # W04-PP-Incremental Discounts at Dog World

    # You run the inventory department at the global retailer, Dog World.   One of your products, a food and water
    # bowl set, has an annual demand of 2500 units per year and they cost you $22 each.  Your inventory holding
    # charge is 25% per year and you estimate it costs about $175 to place an order.   The supplier requires you to
    # order in increments of 10 at a time.

    demand = 2500  # units / yr
    unit_cost = 22  # $ / unit
    holding_charge = 0.25  # % of inventory $ / yr
    ordering_cost = 175  # $ / order

    eoq = EOQ(demand, ordering_cost, unit_cost, holding_charge)
    eoq.summary()


# w04_pp_incremental_discounts()


def w04_ga_01():
    demand = 34954
    ordering_cost = 513
    holding_charge = 0.14
    # unit_cost = 78
    unit_cost = 78 + 0.34

    eoq = EOQ(demand, ordering_cost, unit_cost, holding_charge)
    eoq.summary()


#w04_ga_01()


def w04_pp_dirt_co():
    demand = 12000 * 12
    ordering_cost = 30
    unit_cost = 9.25
    holding_charge = 0.15

    eoq = EOQ(demand, ordering_cost, unit_cost, holding_charge)
    eoq.summary()

    print(eoq.total_relevant_cost())
    print((12000 * 12) / 2400)

# w04_pp_dirt_co()


class Costs:
    @staticmethod
    def purchase_cost(demand, unit_cost):
        return demand * unit_cost

    @staticmethod
    def order_cost(ordering_cost, demand, order_quantity):
        return ordering_cost * (demand / order_quantity)

    @staticmethod
    def holding_cost(holding_charge, unit_cost, order_quantity):
        return (holding_charge * unit_cost) * order_quantity / 2

    @staticmethod
    def shortage_cost():
        #  TODO
        return 0

    @staticmethod
    def total_cost(demand, unit_cost, ordering_cost, order_quantity, holding_charge):
        return (Costs.purchase_cost(demand, unit_cost) +
                Costs.order_cost(ordering_cost, demand, order_quantity) +
                Costs.holding_cost(holding_charge, unit_cost, order_quantity) +
                Costs.shortage_cost())


# demand = 12000 * 12
# ordering_cost = 30
# unit_cost = 10
# holding_charge = 0.15
#
# print(Costs.total_cost(demand, unit_cost, ordering_cost, 2400, 0.15))
# print(Costs.total_cost(demand, 9.25, ordering_cost, 4000, holding_charge))


def w04_ga_02_p1():
    demand = 330 * 12
    ordering_cost = 57+124
    unit_cost = 135
    holding_charge = 0.2

    eoq = EOQ(demand, ordering_cost, unit_cost, holding_charge)
    eoq.summary()


# w04_ga_02_p1()



def w04_pp_08():
    demand = 15000 * 12
    unit_cost = 125
    ordering_cost = 275 + 1250
    holding_charge = 0.25

    eoq = EOQ(demand, ordering_cost, unit_cost, holding_charge)
    eoq.summary()
    print(eoq.total_cost())


w04_pp_08()