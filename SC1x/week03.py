# Week 03

import os

data_dir = '/Users/rhaffey/Desktop/edX/SC1x/data'


def w03_mm_pp_gig_p1():
    import pandas as pd
    import statsmodels.api as sm

    filename = 'W03_MM_PP_Get_Go_data.csv'
    df = pd.read_csv(os.path.join(data_dir, filename))

    X = df['median_income']
    X = sm.add_constant(X)
    y = df['sales_density']

    model = sm.OLS(y, X).fit()
    print(model.summary())


def w03_mm_pp_gig_p2():
    import pandas as pd
    import statsmodels.api as sm

    filename = 'W03_MM_PP_Get_Go_data.csv'
    df = pd.read_csv(os.path.join(data_dir, filename))

    X = df.loc[:, ['median_income', 'median_income_squared']]
    X = sm.add_constant(X)
    y = df['sales_density']

    model = sm.OLS(y, X).fit()
    print(model.summary())


def w03_mm_pp_gig_p3():
    import pandas as pd
    import statsmodels.api as sm

    filename = 'W03_MM_PP_Get_Go_data.csv'
    df = pd.read_csv(os.path.join(data_dir, filename))

    X = df.loc[:, ['median_income', 'median_income_squared', 'new_format']]
    X = sm.add_constant(X)
    y = df['sales_density']

    model = sm.OLS(y, X).fit()
    print(model.summary())


w03_mm_pp_gig_p3()
