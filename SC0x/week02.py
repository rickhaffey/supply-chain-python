# SC0x : Week 02

## Lesson 2

# Banner Chemicals
# - 2 grades: High & Supreme
# - plant capacity: 110 barrels / week

# - components
#   - high grade: 3 gal of A, 1 gal of B per barrel
#   - supreme grade: 2 gal of A, 3 gal of B per barrel

# - supply
#   - A: 300 gal / week
#   - B: 280 gal / week

# - profit margin
#   - high: $80 / barrel
#   - supreme: $200 / barrel

# * Modeling Steps *
# 1. Determine the *decision variables*
# 2. Formulate the *objective function*
#   - must include the decision variables
#   - form of the function determines approach (e.g. LP, IP, etc.)
# 3. Formulate each *constraint*
#   - must include the decision variables
#   - almost always linear


# 1.
#   - Xh (# of high grade barrels to produce / week)
#   - Xs (# of supreme grade barrels to produce / week)
#   - bounds
#       - Xh >= 0
#       - Xs >= 0
#
# 2.
#   - maximize Profit: z(Xh, Xs) = 80 * Xh + 200 * Xs
#
# 3.
#   - plant capacity: Xh + Xs <= 110
#   - supply A: 3 * Xh + 2 * Xs <= 300
#   - supply B: 1 * Xh + 3 * Xs <= 280

from pyomo.environ import *


# pyomo solve SC0x/week02.py --solver=couenne --summary

def recitation_1_a_min():
    # unconstrained (classical) optimization
    # minimize objective function
    model = ConcreteModel()
    model.x = Var(within=Reals)

    def obj(model):
        return model.x ** 2 - 2 * model.x + 3

    model.obj = Objective(rule=obj, sense=minimize)

    return model


def recitation_1_a_max():
    # unconstrained (classical) optimization
    # maximize objective function
    model = ConcreteModel()
    model.x = Var(within=Reals)

    def obj(model):
        return -1 * model.x ** 2 - 2 * model.x + 3

    model.obj = Objective(rule=obj, sense=maximize)

    return model


def recitation_1_a_min_2_var():
    # unconstrained (classical) optimization
    # minimize objective function
    # with 2 decision variables
    model = ConcreteModel()
    model.x1 = Var(within=Reals)
    model.x2 = Var(within=Reals)

    def obj(model):
        return model.x1 ** 2 - model.x1 - model.x2 + model.x2 ** 2

    model.obj = Objective(rule=obj, sense=minimize)

    return model

model = recitation_1_a_min_2_var()
