from scipy.stats import norm
import numpy as np
import math


class UnitNormalLoss:

    @staticmethod
    def g(k):
        return norm.pdf(k) - k * (1 - norm.cdf(k))

    @staticmethod
    def loss_inverse(g_k):
        # see https://stats.stackexchange.com/a/347251/184907

        coefficients = [4.41738119e-09, 1.79200966e-07, 3.01634229e-06,
                        2.63537452e-05, 1.12381749e-04, 5.71289020e-06,
                        -2.64198510e-03, -1.59986142e-02, -5.60399292e-02,
                        -1.48968884e-01, -3.68776346e-01, -1.22551895e+00,
                        -8.99375602e-01]

        result = np.polyval(coefficients, math.log(g_k))

        return round(result, 3)

# g_k = UnitNormalLoss.g(0.0)
# print(g_k)
#
# print(math.log(g_k))
#
# x = np.polyval([4.41738119e-09, 1.79200966e-07, 3.01634229e-06,
#                         2.63537452e-05, 1.12381749e-04, 5.71289020e-06,
#                         -2.64198510e-03, -1.59986142e-02, -5.60399292e-02,
#                         -1.48968884e-01, -3.68776346e-01, -1.22551895e+00,
#                         -8.99375602e-01], math.log(g_k))
# print(x)
