# Week 02

def ape(row, forecast):
    # abs pct err
    err = row['actual'] - row[forecast]
    pct_err = err / row['actual']
    return abs(pct_err)


def w02_mm_pp_general_miles_part01():
    import pandas as pd
    import numpy as np
    df = pd.read_csv('/Users/rhaffey/Desktop/edX/SC1x/data/W02_MM_PP_GeneralMiles_data.csv')

    from statsmodels.tools.eval_measures import rmse
    df['naive_inline'] = df.forecast.shift()
    df['actual'] = df.actual.astype(np.float)
    df['naive_ape'] = df.apply(lambda row: ape(row, 'naive_inline'), axis=1)

    print("naive rmse: {}".format(rmse(df.actual[1:], df.naive_inline[1:])))
    print("naive mape: {}".format(df.naive_ape.mean() * 100))

    df['cumulative_inline'] = df['actual'].expanding().mean().shift()
    mask = df['month'] == 12
    wk12_cum_fcst = df.loc[mask, 'cumulative_inline'].values[0]
    print("week 12 cumulative forecast: {}".format(wk12_cum_fcst))

    df['cumulative_ape'] = df.apply(lambda row: ape(row, 'cumulative_inline'), axis=1)
    print("cumulative rmse: {}".format(rmse(df['actual'][1:], df['cumulative_inline'][1:])))
    print("cumulative mape: {}".format(df.cumulative_ape.mean() * 100))
    print(df)


def w02_mm_pp_ma_and_exp_smoothing():
    import pandas as pd
    from statsmodels.tsa.arima_model import ARMA

    # load the data
    data = {
        "demand": [
            4576,
            5568,
            3240,
            5978,
            5395,
            4644,
            5880,
            6096,
            5967,
            5828,
            5808,
            6076
        ],
        "months": [
            "jan",
            "feb",
            "mar",
            "apr",
            "may",
            "jun",
            "jul",
            "aug",
            "sep",
            "oct",
            "nov",
            "dec"
        ]}
    df = pd.DataFrame(data=data)
    print(df)

    # MA(5)
    model = ARMA(data['demand'], order=(0, 1))
    model_fit = model.fit(disp=False)

    model_fit.predict()

    print(model_fit.predict(len(data['demand']), len(data['demand'])))
    print(model_fit.predict(len(data['demand']) + 1, len(data['demand']) + 1))

    # forecasts using MA(5)
    # exp smoothing w/ alpha = 0.33


def build_w02_mm_pp_ma_ses_data():
    import pandas as pd

    data = {
        "demand": [4576, 5568, 3240, 5978, 5395, 4644, 5880, 6096, 5967, 5828, 5808, 6076],
        "month": ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    }
    s = pd.Series(data=data['demand'], index=data['month'], name='demand')
    s.index.name = 'month'

    return s


def w02_mm_pp_ses_w_statsmodels():
    # NOTE: the ability to provide an initial value isn't available
    # in the currently released version; it looks like 0.10 (unreleased)
    # will support that
    from statsmodels.tsa.holtwinters import SimpleExpSmoothing

    s = build_w02_mm_pp_ma_ses_data()

    # fit model
    model = SimpleExpSmoothing(s.values)
    model_fit = model.fit(smoothing_level=0.33)

    # make prediction
    forecasts = model_fit.predict(3, 13)
    print(forecasts)


def w02_mm_pp_ses():
    import pandas as pd
    import numpy as np

    s = build_w02_mm_pp_ma_ses_data()

    alpha = 0.33

    # create series for forecast and set initial value
    ses_fcst = pd.Series(index=s.index)
    ses_fcst.loc['mar'] = 4951

    x_prev = ses_fcst.loc['mar']
    for (index, value) in ses_fcst['apr':].iteritems():
        x_prev = alpha * s[index] + (1 - alpha) * x_prev
        ses_fcst[index] = x_prev

    # calculate absolute deviation
    ses_abs_err = np.abs(s - ses_fcst.shift())

    df = pd.DataFrame(data={"demand": s, "ses_fcst": ses_fcst, "ses_abs_error": ses_abs_err})
    print(df)

    # calculate mean absolute deviation (MAD) for jun thru dec
    print(df.loc['jun':'dec', 'ses_abs_error'].mean())


def w02_mm_pp_ma5():
    import pandas as pd
    import numpy as np

    # load the data
    data = {
        "demand": [4576, 5568, 3240, 5978, 5395, 4644, 5880, 6096, 5967, 5828, 5808, 6076],
        "month": ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    }
    s = pd.Series(data=data['demand'], index=data['month'], name='demand')
    s.index.name = 'month'

    ma5_fcst = s.rolling(5).mean()
    ma5_err = np.abs(s - ma5_fcst.shift())

    df = pd.DataFrame(data={"demand": s, "ma5_fcst": ma5_fcst, "ma5_abs_err": ma5_err})
    print(df)

    # calculate mean absolute deviation (MAD) for jun thru dec
    print(df.loc['jun':'dec', 'ma5_abs_err'].mean())


def load_sugar_bon_bon_data():
    import pandas as pd
    path = "/Users/rhaffey/Desktop/edX/SC1x/data/W02_MM_PP_SugaBon_data.csv"
    df = pd.read_csv(path, index_col=0)
    return df


def w02_mm_pp_sugar_bon_bon_p1():
    df = load_sugar_bon_bon_data()
    # mean of periods 1-4
    print(df.demand.loc[1:4].mean())


def w02_mm_pp_sugar_bon_bon_p2_3_4():
    import pandas as pd
    import numpy as np

    s = load_sugar_bon_bon_data().demand

    alpha = 0.15

    # create series for forecast and set initial value
    ses_fcst = pd.Series(index=s.index)
    ses_fcst.loc[4] = 205.25

    x_prev = ses_fcst.loc[4]
    for (index, value) in ses_fcst.loc[5:].iteritems():
        x_prev = alpha * s[index] + (1 - alpha) * x_prev
        ses_fcst[index] = x_prev

    # calculate absolute deviation
    ses_abs_err = np.abs(s - ses_fcst.shift())
    ses_abs_pct_err = ses_abs_err / s

    df = pd.DataFrame(data={
        "demand": s,
        "ses_fcst": ses_fcst,
        "ses_abs_error": ses_abs_err,
        "ses_abs_pct_err": ses_abs_pct_err
    })

    print(df)

    print("MAPE: {}".format(df.ses_abs_pct_err.loc[5:24].mean()))


def w02_mm_pp_sugar_bon_bon_p5():
    import matplotlib as mpl
    mpl.use('TkAgg')

    import matplotlib.pyplot as plt

    s = load_sugar_bon_bon_data().demand

    plt.scatter(s.index, s)
    plt.show()


w02_mm_pp_sugar_bon_bon_p5()
