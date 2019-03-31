# import pytest
# import numpy as np
# from unitnormalloss import UnitNormalLoss
#
#
# # assert 2.2 == pytest.approx(2.3)
# # # fails, default is ± 2.3e-06
# # assert 2.2 == pytest.approx(2.3, 0.1)
# # # passes
# #
# # # also works the other way, in case you were worried:
# # assert pytest.approx(2.3, 0.1) == 2.2
# # # passes
#
#
# def test_round_trip_from_k():
#     ks = np.linspace(start=-3.99, stop=3.99, num=799)
#     for k in ks:
#         g_k = UnitNormalLoss.g(k)
#         result = UnitNormalLoss.loss_inverse(g_k)
#         print("k: {}, g_k: {}, result: {}".format(k, g_k, result))
#         assert result == pytest.approx(k, 0.01)
