from demand import Demand
from rawcosts import RawCosts
from eoq import EOQ


def part3():
    d = Demand(240, 'M')
    rc = RawCosts(50.0, 100.0, 0.01, holding_time_unit='M')
    Q = EOQ.optimal_order_quantity(rc, d)
    print(Q)

    T = EOQ.optimal_cycle_time(rc, d)
    print(T)

    print(T * 4)


part3()
