# maximize Profit = (price * MIN[x, Q]) - c * Q


import pandas as pd
from scipy.stats import norm


class DataTable:
    def __init__(self, mean_demand, stddev_demand, price, cost):
        self.mean_demand = mean_demand
        self.stddev_demand = stddev_demand
        self.price = price
        self.cost = cost

        self.df = self.__build_demand_probabilities__()
        self.__build_weighted_profit_columns__()

    def __weighted_profit__(self, row, ordered):
        demand = row['demand']
        sold = min(demand, ordered)
        prob = row['probability']
        return (self.price * sold - self.cost * ordered) * prob

    def __build_weighted_profit_columns__(self):
        o_cols = []
        for i in range(1, self.df['demand'].max() + 1):
            col_name = 'o_{}'.format(i)
            o_cols.append(col_name)
            self.df[col_name] = self.df.apply(lambda row: self.__weighted_profit__(row, i), axis=1)

    def __build_demand_probabilities__(self):
        index = 0
        demand = [-1]
        cum_prob = [0]
        probability = [0]

        while cum_prob[index] < 0.9999:
            index += 1
            demand.append(index - 1)
            cum_prob.append(norm.cdf(demand[index], loc=self.mean_demand,
                                     scale=self.stddev_demand))
            # estimate discrete prob based on cumulative, continuous probs
            probability.append(cum_prob[index] - cum_prob[index - 1])

        return pd.DataFrame({
            "demand": demand[1:],
            "probability": probability[1:],
            "cum_prob": cum_prob[1:]
        })

    def display_optimal(self):
        totals = self.df.loc[:, self.df.columns[3:]].sum()
        max_value = totals.max()
        print(totals[totals == max_value])


DataTable(32, 11, 24.00, 10.90).display_optimal()
