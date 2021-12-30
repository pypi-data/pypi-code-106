import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data_tool import cal_date
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


class BacktestHandle:

    def weight2d(self, df_weight, df_ret_d):
        df_weight.fillna(0, inplace=True)
        inter_cols = set(df_ret_d.columns).intersection(df_weight.columns)
        df_ret_d = df_ret_d[inter_cols]
        df_weight = df_weight[inter_cols]
        df_weight_d_list = []
        for i in range(1, len(df_weight)):
            start = df_weight.index[i - 1]
            end = df_weight.index[i]
            df_ret_d_tmp = df_ret_d[(df_ret_d.index >= start) & (df_ret_d.index < end)]
            df_weight_d_tmp = df_weight[df_weight.index == start].reindex()
            df_ret_d_tmp.iloc[0] = 0
            df_ret_d_tmp = (df_ret_d_tmp + 1).cumprod()
            df_weight_d_tmp = df_ret_d_tmp * df_weight_d_tmp.values
            df_weight_d_tmp = df_weight_d_tmp.div(df_weight_d_tmp.sum(axis=1), axis=0)
            df_weight_d_list.append(df_weight_d_tmp)
        df_weight_d_tmp = df_weight[df_weight.index == end]
        df_ret_d_tmp = df_ret_d[df_ret_d.index >= end]
        df_ret_d_tmp.iloc[0] = 0
        df_ret_d_tmp = (df_ret_d_tmp + 1).cumprod()
        df_weight_d_tmp = df_ret_d_tmp * df_weight_d_tmp.values
        df_weight_d_tmp = df_weight_d_tmp.div(df_weight_d_tmp.sum(axis=1), axis=0)
        df_weight_d_list.append(df_weight_d_tmp)
        df_weight_d = pd.concat(df_weight_d_list, axis=0)
        return df_weight_d

    def weight2d_equal(self, df_weight):
        end_date = datetime.datetime.now().date().strftime('%Y-%m-%d')
        trade_dates = pd.Series(cal_date('2009-01-01', end_date, period='D'))
        df_weight.index = list(map(lambda x: trade_dates[trade_dates.index(x) - 1], df_weight.index))  # 得到调仓日
        df_weight = df_weight.reindex(trade_dates)
        df_weight.fillna(method='ffill', inplace=True)
        df_weight.div(df_weight.sum(axis=1), axis=0)
        return df_weight

    def backtest(self, df_weight, df_next_ret, fee_rate=0.001, model=0, show=True):
        df_next_ret = df_next_ret[df_next_ret.index >= df_weight.index[0]]
        # 构造交易权重矩阵
        df_turnover = df_weight.diff().fillna(0)
        df_fee = (np.abs(df_turnover) * fee_rate)
        df_ret = df_next_ret * df_weight - df_fee
        df_ret = df_ret.sum(axis=1)
        if show:
            df_pnl = df_ret.cumsum() if model == 0 else (1 + df_ret).cumprod()
            df_pnl.plot()
            plt.show()
            return df_ret, df_pnl
        else:
            return df_ret
