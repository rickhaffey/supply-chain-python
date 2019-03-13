# you'll need scipy, numpy, and pandas installed:
# pip install scipy, numpy, pandas

from scipy.stats import norm
import pandas as pd
import numpy as np


# unit normal loss function
def g(k):
    return norm.pdf(k) - k * (1 - norm.cdf(k))


def format(k):
    return "{:.2f}".format(k)


def build_df():
    ks = np.linspace(start=-3.99, stop=3.99, num=799)
    probabilities = {format(k): norm.cdf(k) for k in ks}
    losses = {k: g(k) for k in ks}

    result = pd.DataFrame(data={
        "P[u<k]": probabilities,
        "G(k)": losses
    })
    result.index.name = "k"
    return result


def find_g_k(df, k):
    return df.loc[k]['G(k)']


def find_k_from_g_k(df, g_k):
    col = 'G(k)'

    # check for an exact match
    eq_mask = df[col] == g_k
    if any(eq_mask.values):
        eq = df[eq_mask].index[0]
    else:
        eq = None

    lt = df[df[col].lt(g_k)].index[0]
    gt = df[df[col].gt(g_k)].index[-1]

    return lt, eq, gt


df = build_df()
# print(df)


print(find_k_from_g_k(df, 0.991370))
# print(find_g_k(df, -0.88))
# TODO: using float as index on df is problematic, but also
#  need a mechanism for sorting index values (lt/gt) numerically
