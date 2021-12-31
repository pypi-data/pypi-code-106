from __future__ import (absolute_import, division, print_function, unicode_literals)

import pandas as pd
import datetime as dt
from datetime import timezone
import talib
from dataclasses import dataclass
import numpy
import time

from bokeh.plotting import figure, show, ColumnDataSource
from bokeh.io import output_notebook
from bokeh.models import NumeralTickFormatter, DatetimeTickFormatter, HoverTool
output_notebook()


class Config:
   def __init__(self):
      self.__debug = False
      self.__taker_fee_rate = 0.0005
      self.__funding_rate = 0.0001
      self.__funding_rate_interval = 28800

   @property
   def debug(self):
      return self.__debug

   @debug.setter
   def debug(self, value: bool):
      self.__debug = value

   @property
   def taker_fee_rate(self):
      return self.__taker_fee_rate

   @taker_fee_rate.setter
   def taker_fee_rate(self, value: float):
      self.__taker_fee_rate = value

   @property
   def funding_rate(self):
      return self.__funding_rate

   @funding_rate.setter
   def funding_rate(self, value: float):
      self.__funding_rate = value

   @property
   def funding_rate_interval(self):
      return self.__funding_rate_interval

   @funding_rate_interval.setter
   def funding_rate_interval(self, value: int):
      self.__funding_rate_interval = value


@dataclass(frozen=True)
class OHLCData:
   symbol: str
   files: list
   timestamp: int
   datetime: str
   open: float
   high: float
   low: float
   close: float
   volume: float
   timeframe: str
   compression: str = ""
   dtformat: str = "%Y-%m-%d %H:%M:%S"
   tsformat: str = "s"  # D,s,ms,us,ns
   separator: str = ","
   header: int = 0
   ascending: bool = True


@dataclass(frozen=True)
class Indicator:
   name: str
   tag: str
   timeframe: str
   period: int


@dataclass
class Position:
   side: str
   leverage: int
   open_price: float
   liquidation_price: float
   size: float
   notional: float
   margin: float
   created_at: pd.Timestamp
   updated_at: pd.Timestamp
   stop_price: float = 0
   take_profit_price: float = 0


class Portfolio:
   def __init__(self):
      self.__cash = 0
      self.__futures = 0

   @property
   def cash(self):
      return self.__cash

   @cash.setter
   def cash(self, amount: float):
      self.__cash = amount

   def add_cash(self, amount: float):
      self.__cash += amount

   def sub_cash(self, amount: float):
      self.__cash -= amount

   @property
   def futures(self):
      return self.__futures

   @futures.setter
   def futures(self, amount: float):
      self.__futures = amount

   def add_futures(self, amount: float):
      self.__futures += amount

   def sub_futures(self, amount: float):
      self.__futures -= amount

   @property
   def total_value(self):
      return self.__cash + self.__futures


class Store:
   def __init__(self):
      self.__ohlc_data = None
      self.__series_data = None
      self.__portfolio_history = []
      self.__ledger_records = []
      self.__trades = []
      self.__indicators_history = []

   @property
   def ohlc_data(self):
      return self.__ohlc_data

   @ohlc_data.setter
   def ohlc_data(self, data: pd.DataFrame):
      self.__ohlc_data = data

   @property
   def series_data(self):
      return self.__series_data

   @series_data.setter
   def series_data(self, data: pd.DataFrame):
      self.__series_data = data

   def clear_series_data(self):
      self.__series_data = None

   @property
   def ledger_records(self):
      return self.__ledger_records

   def add_ledger_record(self, row: list):
      self.__ledger_records.append(row)

   @property
   def trades(self):
      return self.__trades

   def add_trade(self, row: list):
      self.__trades.append(row)

   @property
   def portfolio_history(self):
      return self.__portfolio_history

   def add_portfolio_history(self, row: list):
      if row[0].hour == 0 and row[0].minute == 0:
         self.__portfolio_history.append(row)

   @property
   def indicators_history(self):
      return self.__indicators_history

   def add_indicators_history(self, values: dict):
      self.__indicators_history.append(values)

   def clear_history(self):
      self.__portfolio_history = []
      self.__ledger_records = []
      self.__trades = []
      self.__indicators_history = []


class Report(object):
   def __init__(self, symbol: str, strategy: str, start_cash: float, duration: dt.timedelta, store: Store, portfolio: Portfolio):
      self.__symbol = symbol
      self.__strategy = strategy
      self.__start_cash = start_cash
      self.__duration = duration
      self.__store = store
      self.__portfolio = portfolio

      self.__portfolio_history = self.PortfolioHistory(
          data=pd.DataFrame(
              store.portfolio_history,
              columns=["datetime", "cash", "futures", "total"]
          ).set_index("datetime").fillna(method='ffill').round({"cash": 2, "futures": 2, "total": 2})
      )

      self.__ledger_records = pd.DataFrame(
          self.__store.ledger_records,
          columns=["datetime", "type", "amount", "asset"]
      ).round({"amount": 2})

      self.__trades = pd.DataFrame(
          self.__store.trades,
          columns=["datetime", "side", "amount", "price", "notional", "fee"]
      ).round({"amount": 2, "price": 2, "notional": 2, "fee": 2})

   @property
   def portfolio_history(self):
      return self.__portfolio_history

   def info(self):
      template = """
			Symbol: {symbol}
			Period: {from_date} - {to_date} ({from_ts} - {to_ts})
			Strategy: {strategy}

			Start Portfolio:
			Cash: {start_cash}
			Futures: 0
			Total: {start_portfolio}

			End Portfolio:
			Cash: {end_cash}
			Futures: {end_futures}
			Total: {end_portfolio}

			Max. Portfolio: {max_portfolio}
			Min. Portfolio: {min_portfolio}
			Profit: {profit_amount} ({profit_percent}%)
			Avg. Daily Profit: {avg_daily_profit}%
			Avg. Monthly Profit: {avg_monthly_profit}%
			Avg. Annual Profit: {avg_annual_profit}%
			Total Trades Qty: {total_trades_qty}
			Duration: {duration}
		"""

      first = self.__store.ohlc_data.iloc[0]
      last = self.__store.ohlc_data.iloc[-1]
      profit_amount = self.__portfolio.total_value - self.__start_cash

      msg = template.format(
          symbol=self.__symbol,
          from_date=first.name.strftime('%d-%m-%Y'),
          to_date=last.name.strftime('%d-%m-%Y'),
          from_ts=int(time.mktime(first.name.timetuple())),
          to_ts=int(time.mktime(last.name.timetuple())),
          strategy=self.__strategy,
          start_portfolio=round(self.__start_cash, 2),
          start_cash=round(self.__start_cash, 2),
          end_portfolio=round(self.__portfolio.total_value, 2),
          end_cash=round(self.__portfolio.cash, 2),
          end_futures=round(self.__portfolio.futures, 2),
          max_portfolio=self.portfolio_history.data.total.max(),
          min_portfolio=self.portfolio_history.data.total.min(),
          profit_amount=round(profit_amount, 2),
          profit_percent=round((profit_amount / self.__start_cash) * 100, 1),
          avg_daily_profit=round(self.portfolio_history.data.pct_change(periods=1).total.mean() * 100, 2),
          avg_monthly_profit=round(self.portfolio_history.data.pct_change(periods=30).total.mean() * 100, 2),
          avg_annual_profit=round(self.portfolio_history.data.pct_change(periods=365).total.mean() * 100, 2),
          total_trades_qty=len(self.__trades.index),
          duration=self.__duration
      )

      print(msg)

   @property
   def ledger_records(self):
      return self.__ledger_records

   @property
   def trades(self):
      return self.__trades

   class PortfolioHistory(object):
      def __init__(self, data: pd.DataFrame):
         self.__data = data

      @property
      def data(self):
         return self.__data

      def plot(self):
         source = ColumnDataSource(data=self.__data.reset_index())
         tools = "pan,wheel_zoom,reset,save"

         p = figure(
             width=1000,
             height=400,
             tools=tools,
             title="Portfolio History",
             x_axis_label='Date',
             y_axis_label='Amount',
             x_axis_type="datetime",
             active_scroll="wheel_zoom",
             toolbar_location="above"
         )

         cash_p = p.line("datetime", "cash", source=source, legend_label="Cash", line_width=1, line_color="red")

         cash_hover = HoverTool(
             renderers=[cash_p],
             tooltips=[
                 ("Date", "@datetime{%Y-%m-%d}"),
                 ("Amount", "@cash{%0.2f}")
             ],
             formatters={
                 "@datetime": "datetime",
                 "@cash": "printf",
             },
             mode="vline"
         )

         p.add_tools(cash_hover)
         futures_p = p.line("datetime", "futures", source=source, legend_label="Futures", line_width=1, line_color="orange")

         futures_hover = HoverTool(
             renderers=[futures_p],
             tooltips=[
                 ("Date", "@datetime{%Y-%m-%d}"),
                 ("Amount", "@futures{%0.2f}")
             ],
             formatters={
                 "@datetime": "datetime",
                 "@futures": "printf",
             },
             mode="vline"
         )

         p.add_tools(futures_hover)
         total_p = p.line("datetime", "total", source=source, legend_label="Total", line_width=1, line_color="green")

         total_hover = HoverTool(
             renderers=[total_p],
             tooltips=[
                 ("Date", "@datetime{%Y-%m-%d}"),
                 ("Amount", "@total{%0.2f}")
             ],
             formatters={
                 "@datetime": "datetime",
                 "@total": "printf",
             },
             mode="vline"
         )

         p.add_tools(total_hover)
         p.legend.location = "top_left"
         p.xaxis[0].formatter = DatetimeTickFormatter(years="%Y", months="%Y-%m", days="%Y-%m-%d", hours="%Y-%m-%d %H:%M", minutes="%Y-%m-%d %H:%M")
         p.yaxis[0].formatter = NumeralTickFormatter(format="0.00")
         show(p)


class Backtrader(object):
   def __init__(self):
      self.__symbol = None
      self.__ohlc_timeframes = ["1m", "5m", "15m", "30m", "1h", "2h", "3h", "4h", "6h", "12h", "1D", "1W"]
      self.__ohlc_timeframe = None
      self.__start_cash = 0
      self.cfg = Config()
      self.store = Store()
      self.portfolio = Portfolio()
      self.strategy = self.Strategy(self)

   def __resample_ohlc_data(self, data: pd.DataFrame, timeframe: str):
      if data.empty:
         raise Exception("OHLC data is empty.")

      item = {
          "open": "first",
          "high": "max",
          "low": "min",
          "close": "last",
          "volume": "sum"
      }

      if timeframe == "1m":
         return data
      elif timeframe == "5m":
         return data.resample("5Min").agg(item)
      elif timeframe == "15m":
         return data.resample("15Min").agg(item)
      elif timeframe == "30m":
         return data.resample("30Min").agg(item)
      elif timeframe == "1h":
         return data.resample("60Min").agg(item)
      elif timeframe == "2h":
         return data.resample("120Min").agg(item)
      elif timeframe == "3h":
         return data.resample("180Min").agg(item)
      elif timeframe == "4h":
         return data.resample("240Min").agg(item)
      elif timeframe == "6h":
         return data.resample("360Min").agg(item)
      elif timeframe == "12h":
         return data.resample("720Min").agg(item)
      elif timeframe == "1D":
         return data.resample("D").agg(item)
      elif timeframe == "1W":
         return data.resample("W-MON").agg(item)

      return data

   def debug_mode(self, enabled: bool):
      self.cfg.debug = enabled

   def set_taker_fee_rate(self, percent: float):
      self.cfg.taker_fee_rate = percent / 100

   def set_cash(self, amount: float):
      self.__start_cash = amount
      self.portfolio.cash = amount

   def set_funding_rate(self, percent: float):
      self.cfg.funding_rate = percent / 100

   def set_funding_rate_interval(self, seconds: int):
      self.cfg.funding_rate_interval = seconds

   def set_decimals(self, value: int):
      self.cfg.decimals = value

   def is_first_min_of_timeframe(self, ts: pd.Timestamp, timeframe: str):
      if timeframe == "1m":
         return True
      elif timeframe == "5m":
         if ts.minute in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]:
            return True
      elif timeframe == "15m":
         if ts.minute in [0, 15, 30, 45]:
            return True
      elif timeframe == "30m":
         if ts.minute in [0, 30]:
            return True
      elif timeframe == "1h":
         if ts.minute == 0:
            return True
      elif timeframe == "2h":
         if ts.hour in [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22] and ts.minute == 0:
            return True
      elif timeframe == "3h":
         if ts.hour in [0, 3, 6, 9, 12, 15, 18, 21] and ts.minute == 0:
            return True
      elif timeframe == "4h":
         if ts.hour in [0, 4, 8, 12, 16, 20] and ts.minute == 0:
            return True
      elif timeframe == "6h":
         if ts.hour in [0, 6, 12, 18] and ts.minute == 0:
            return True
      elif timeframe == "12h":
         if ts.hour in [0, 12] and ts.minute == 0:
            return True
      elif timeframe == "1D":
         if ts.hour == 0 and ts.minute == 0:
            return True
      elif timeframe == "1W":
         if ts.weekday() == 0 and ts.hour == 0 and ts.minute == 0:
            return True

      return False

   def is_last_min_of_timeframe(self, ts: pd.Timestamp, timeframe: str):
      if timeframe == "1m":
         return True
      elif timeframe == "5m":
         if ts.minute in [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59]:
            return True
      elif timeframe == "15m":
         if ts.minute in [14, 29, 44, 59]:
            return True
      elif timeframe == "30m":
         if ts.minute in [29, 59]:
            return True
      elif timeframe == "1h":
         if ts.minute == 59:
            return True
      elif timeframe == "2h":
         if ts.hour in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23] and ts.minute == 59:
            return True
      elif timeframe == "3h":
         if ts.hour in [2, 5, 8, 11, 14, 17, 20, 23] and ts.minute == 59:
            return True
      elif timeframe == "4h":
         if ts.hour in [3, 7, 11, 15, 19, 23] and ts.minute == 59:
            return True
      elif timeframe == "6h":
         if ts.hour in [5, 11, 17, 23] and ts.minute == 59:
            return True
      elif timeframe == "12h":
         if ts.hour in [11, 23] and ts.minute == 59:
            return True
      elif timeframe == "1D":
         if ts.hour == 23 and ts.minute == 59:
            return True
      elif timeframe == "1W":
         if ts.weekday() == 6 and ts.hour == 23 and ts.minute == 59:
            return True

      return False

   def get_candle_open_timestamp(self, ts: pd.Timestamp, timeframe: str):
      n = 0

      if timeframe == "1m":
         n = ts.minute % 1
      elif timeframe == "5m":
         n = ts.minute % 5
      elif timeframe == "15m":
         n = ts.minute % 15
      elif timeframe == "30m":
         n = ts.minute % 30
      elif timeframe == "1h":
         n = ts.minute % 60
      elif timeframe == "2h":
         n = ((ts.hour % 2) * 60) + (ts.minute % 60)
      elif timeframe == "3h":
         n = ((ts.hour % 3) * 60) + (ts.minute % 60)
      elif timeframe == "4h":
         n = ((ts.hour % 4) * 60) + (ts.minute % 60)
      elif timeframe == "6h":
         n = ((ts.hour % 6) * 60) + (ts.minute % 60)
      elif timeframe == "12h":
         n = ((ts.hour % 12) * 60) + (ts.minute % 60)
      elif timeframe == "1D":
         n = ((ts.hour % 24) * 60) + (ts.minute % 60)
      elif timeframe == "1W":
         n = ((ts.weekday() % 7) * 1440) + ((ts.hour % 24) * 60) + (ts.minute % 60)

      return ts - pd.Timedelta(n, unit="m")

   def get_prev_candle_open_timestamp(self, ts: pd.Timestamp, timeframe: str):
      n = self.get_candle_open_timestamp(ts, timeframe)

      if timeframe == "1m":
         return n - pd.Timedelta(60, unit="sec")
      elif timeframe == "5m":
         return n - pd.Timedelta(300, unit="sec")
      elif timeframe == "15m":
         return n - pd.Timedelta(900, unit="sec")
      elif timeframe == "30m":
         return n - pd.Timedelta(1800, unit="sec")
      elif timeframe == "1h":
         return n - pd.Timedelta(3600, unit="sec")
      elif timeframe == "2h":
         return n - pd.Timedelta(7200, unit="sec")
      elif timeframe == "3h":
         return n - pd.Timedelta(10800, unit="sec")
      elif timeframe == "4h":
         return n - pd.Timedelta(14400, unit="sec")
      elif timeframe == "6h":
         return n - pd.Timedelta(21600, unit="sec")
      elif timeframe == "12h":
         return n - pd.Timedelta(43200, unit="sec")
      elif timeframe == "1D":
         return n - pd.Timedelta(86400, unit="sec")
      elif timeframe == "1W":
         return n - pd.Timedelta(604800, unit="sec")

      return n

   def get_timeframe_timedelta(self, timeframe: str):
      if timeframe == "1m":
         return pd.Timedelta(60, unit="sec")
      elif timeframe == "5m":
         return pd.Timedelta(300, unit="sec")
      elif timeframe == "15m":
         return pd.Timedelta(900, unit="sec")
      elif timeframe == "30m":
         return pd.Timedelta(1800, unit="sec")
      elif timeframe == "1h":
         return pd.Timedelta(3600, unit="sec")
      elif timeframe == "2h":
         return pd.Timedelta(7200, unit="sec")
      elif timeframe == "3h":
         return pd.Timedelta(10800, unit="sec")
      elif timeframe == "4h":
         return pd.Timedelta(14400, unit="sec")
      elif timeframe == "6h":
         return pd.Timedelta(21600, unit="sec")
      elif timeframe == "12h":
         return pd.Timedelta(43200, unit="sec")
      elif timeframe == "1D":
         return pd.Timedelta(86400, unit="sec")
      elif timeframe == "1W":
         return pd.Timedelta(604800, unit="sec")

   def add_ohlc_data(self, data: OHLCData):
      if data.timestamp == -1 and data.datetime == -1:
         raise Exception("Timestamp or datetime column is required.")

      self.__symbol = data.symbol
      usecols = []

      if data.datetime >= 0:
         usecols.append(data.datetime)
      else:
         usecols.append(data.timestamp)

      usecols = usecols + [data.open, data.high, data.low, data.close, data.volume]
      dfs = (pd.read_csv(f, sep=data.separator, header=data.header, usecols=usecols) for f in data.files)
      df = pd.concat(dfs, ignore_index=False)

      cols = {
          "open": data.open,
          "high": data.high,
          "low": data.low,
          "close": data.close,
          "volume": data.volume
      }

      if data.datetime >= 0:
         cols["datetime"] = data.datetime
      else:
         cols["timestamp"] = data.timestamp

      sorted_cols = sorted(cols.items(), key=lambda x: x[1], reverse=False)
      columns = {}

      for i, col in enumerate(sorted_cols):
         columns[df.columns[i]] = col[0]

      df = df.rename(columns=columns)

      if data.datetime >= 0:
         df["datetime"] = pd.to_datetime(df["datetime"], format=data.dtformat, utc=True)
      else:
         df["datetime"] = pd.to_datetime(df["timestamp"], unit=data.tsformat, utc=True)

      df = df.sort_values("datetime", ascending=data.ascending).set_index("datetime")

      if data.compression != "" and data.timeframe != data.compression:
         from_idx = self.__ohlc_timeframes.index(data.timeframe)
         to_idx = self.__ohlc_timeframes.index(data.compression)

         if to_idx > from_idx:
            df = self.__resample_ohlc_data(df, data.compression)
            self.__ohlc_timeframe = data.compression
         else:
            raise Exception(f"Timeframe compression from {data.timeframe} to {data.compression} is not possible.")
      else:
         self.__ohlc_timeframe = data.timeframe

      self.store.ohlc_data = df

   def set_strategy(self, strategy):
      self.store.clear_series_data()

      if self.store.ohlc_data is None or self.store.ohlc_data.empty:
         raise Exception("OHLC data is empty.")

      self.__strategy = strategy(self)
      series_data = self.store.ohlc_data

      if self.__strategy.indicators is not None and len(self.__strategy.indicators) > 0:
         for ind in self.__strategy.indicators:
            ind_tf_idx = self.__ohlc_timeframes.index(ind.timeframe)
            ohlc_tf_idx = self.__ohlc_timeframes.index(self.__ohlc_timeframe)

            if ohlc_tf_idx > ind_tf_idx:
               raise Exception(f"Indicator timeframe must be less than or equal OHLC data timeframe.")

            resampled = self.__resample_ohlc_data(self.store.ohlc_data, ind.timeframe)
            indexes = numpy.array(resampled.index.values)
            df = pd.DataFrame(index=indexes)

            if ind.name == "EMA":
               if len(resampled.close) < ind.period:
                  raise Exception(f"OHLC data is not enough for period {ind.period}.")

               close = numpy.array(resampled.close, dtype=float)
               nans = numpy.isnan(close)
               df[ind.tag] = pd.Series(talib.EMA(close[~nans], timeperiod=ind.period), index=indexes[~nans])
            elif ind.name == "CCI":
               if len(resampled.close) < ind.period:
                  raise Exception(f"OHLC data is not enough for period {ind.period}.")

               high = numpy.array(resampled.high, dtype=float)
               low = numpy.array(resampled.low, dtype=float)
               close = numpy.array(resampled.close, dtype=float)
               nans = numpy.isnan(close)

               df[ind.tag] = pd.Series(
                   talib.CCI(
                       high[~nans],
                       low[~nans],
                       close[~nans],
                       timeperiod=ind.period
                   ),
                   index=indexes[~nans]
               )
            elif ind.name == "ATR":
               if len(resampled.close) < ind.period + 1:
                  raise Exception(f"OHLC data is not enough for period {ind.period}.")

               high = numpy.array(resampled.high, dtype=float)
               low = numpy.array(resampled.low, dtype=float)
               close = numpy.array(resampled.close, dtype=float)
               nans = numpy.isnan(close)

               df[ind.tag] = pd.Series(
                   talib.ATR(
                       high[~nans],
                       low[~nans],
                       close[~nans],
                       timeperiod=ind.period
                   ),
                   index=indexes[~nans]
               )

            df.index += self.get_timeframe_timedelta(ind.timeframe)
            df.index = df.index.tz_localize('UTC')
            series_data = pd.concat([series_data, df], ignore_index=False, axis=1)

      self.store.series_data = series_data.fillna(method='ffill')

   def run(self) -> Report:
      self.store.clear_history()
      self.portfolio.cash = self.__start_cash
      self.portfolio.futures = 0
      self.__strategy.position = None

      if self.portfolio.cash == 0:
         raise Exception("Insufficient funds.")

      if self.__strategy is None:
         raise Exception("Strategy is not set.")

      start = dt.datetime.now(timezone.utc)

      for row in self.store.series_data.itertuples():
         pos_size = 0

         if self.__strategy.position is not None:
            pos_size = self.__strategy.position.size

         self.__strategy.last_series = row
         self.__strategy.handle_stop_order()
         self.__strategy.handle_take_profit_order()
         self.__strategy.next()
         self.portfolio.futures = row.close * pos_size
         self.store.add_portfolio_history([row.Index, self.portfolio.cash, self.portfolio.futures, self.portfolio.total_value])

      end = dt.datetime.now(timezone.utc)
      duration = end - start

      return Report(
          symbol=self.__symbol,
          strategy=self.__strategy.name,
          start_cash=self.__start_cash,
          duration=duration,
          store=self.store,
          portfolio=self.portfolio
      )

   class Strategy(object):
      def __init__(self, ctx):
         self.name = None
         self.ctx = ctx
         self.indicators = None
         self.position = None
         self.last_series = None

      def log(self, msg: str):
         if self.ctx.cfg.debug:
            ts = self.last_series.Index.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{ts} * {msg}")

      def get_liquidation_price(self, side: str, leverage: int, open_price: float):
         if side == "long":
            return (open_price * leverage) / (leverage + 1 - (0.01 * leverage))
         elif side == "short":
            return (open_price * leverage) / (leverage - 1 + (0.01 * leverage))

         return None

      def handle_stop_order(self):
         if self.position is not None:
            if self.position.stop_price > 0:
               if self.position.side == "long":
                  if self.last_series.low <= self.position.stop_price:
                     pnl = (self.position.stop_price - self.position.open_price) * self.position.size
                     notional = self.position.stop_price * self.position.size
                     fee = notional * self.ctx.cfg.taker_fee_rate
                     self.ctx.portfolio.add_cash(self.position.margin + pnl - fee)
                     self.ctx.store.add_trade([self.last_series.Index, "sell", self.position.size, self.position.stop_price, notional, fee])
                     self.ctx.store.add_ledger_record([self.last_series.Index, "realized_pnl", pnl, "USD"])
                     self.ctx.store.add_ledger_record([self.last_series.Index, "commission", fee * -1, "USD"])

                     if self.indicators is not None:
                        ind_values = {"datetime": self.last_series.Index}

                        for k, v in self.last_series[-len(self.indicators):].iteritems():
                           ind_values[k] = v

                        self.ctx.store.add_indicators_history(ind_values)

                     self.position = None

                     self.log("STOP LOSS - Side: SELL, Position Side: LONG, Price: %f, Size: %f, Notional: %f, Fee: %f USD" % (
                         self.position.stop_price, self.position.size, notional, fee * -1
                     ))
               elif self.position.side == "short":
                  if self.last_series.high >= self.position.stop_price:
                     pnl = (self.position.open_price - self.position.stop_price) * self.position.size
                     notional = self.position.stop_price * self.position.size
                     fee = notional * self.ctx.cfg.taker_fee_rate
                     self.ctx.portfolio.add_cash(self.position.margin + pnl - fee)
                     self.ctx.store.add_trade([self.last_series.Index, "buy", self.position.size, self.position.stop_price, notional, fee])
                     self.ctx.store.add_ledger_record([self.last_series.Index, "realized_pnl", pnl, "USD"])
                     self.ctx.store.add_ledger_record([self.last_series.Index, "commission", fee * -1, "USD"])

                     if self.indicators is not None:
                        ind_values = {"datetime": self.last_series.Index}

                        for k, v in self.last_series[-len(self.indicators):].iteritems():
                           ind_values[k] = v

                        self.ctx.store.add_indicators_history(ind_values)

                     self.position = None

                     self.log("STOP LOSS - Side: BUY, Position Side: SHORT, Price: %f, Size: %f, Notional: %f, Fee: %f USD" % (
                         self.position.stop_price, self.position.size, notional, fee * -1
                     ))

      def handle_take_profit_order(self):
         if self.position is not None:
            if self.position.take_profit_price > 0:
               if self.position.side == "long":
                  if self.last_series.high >= self.position.take_profit_price:
                     pnl = (self.position.take_profit_price - self.position.open_price) * self.position.size
                     notional = self.position.take_profit_price * self.position.size
                     fee = notional * self.ctx.cfg.taker_fee_rate
                     self.ctx.portfolio.add_cash(self.position.margin + pnl - fee)
                     self.ctx.store.add_trade([self.last_series.Index, "sell", self.position.size, self.position.take_profit_price, notional, fee])
                     self.ctx.store.add_ledger_record([self.last_series.Index, "realized_pnl", pnl, "USD"])
                     self.ctx.store.add_ledger_record([self.last_series.Index, "commission", fee * -1, "USD"])

                     if self.indicators is not None:
                        ind_values = {"datetime": self.last_series.Index}

                        for k, v in self.last_series[-len(self.indicators):].iteritems():
                           ind_values[k] = v

                        self.ctx.store.add_indicators_history(ind_values)

                     self.position = None

                     self.log("TAKE PROFIT - Side: SELL, Position Side: LONG, Price: %f, Size: %f, Notional: %f, Fee: %f USD" % (
                         self.position.take_profit_price, self.position.size, notional, fee * -1
                     ))
               elif self.position.side == "short":
                  if self.last_series.low <= self.position.take_profit_price:
                     pnl = (self.position.open_price - self.position.take_profit_price) * self.position.size
                     notional = self.position.take_profit_price * self.position.size
                     fee = notional * self.ctx.cfg.taker_fee_rate
                     self.ctx.portfolio.add_cash(self.position.margin + pnl - fee)
                     self.ctx.store.add_trade([self.last_series.Index, "buy", self.position.size, self.position.take_profit_price, notional, fee])
                     self.ctx.store.add_ledger_record([self.last_series.Index, "realized_pnl", pnl, "USD"])
                     self.ctx.store.add_ledger_record([self.last_series.Index, "commission", fee * -1, "USD"])

                     if self.indicators is not None:
                        ind_values = {"datetime": self.last_series.Index}

                        for k, v in self.last_series[-len(self.indicators):].iteritems():
                           ind_values[k] = v

                        self.ctx.store.add_indicators_history(ind_values)

                     self.position = None

                     self.log("TAKE PROFIT - Side: BUY, Position Side: SHORT, Price: %f, Size: %f, Notional: %f, Fee: %f USD" % (
                         self.position.take_profit_price, self.position.size, notional, fee * -1
                     ))

      def buy(self, size: float, leverage: int = 1, stop_price: float = 0, take_profit_price: float = 0, reduce_only: bool = False):
         if size == 0:
            raise Exception("Size must be greater zero.")

         if reduce_only:
            if self.position is not None:
               if self.position.side != "short":
                  raise Exception("Wrong side for reduce only position.")

               pnl = (self.position.open_price - self.last_series.close) * size
               notional = self.last_series.close * size
               fee = notional * self.ctx.cfg.taker_fee_rate
               margin = notional * (1 / self.position.leverage)
               self.ctx.portfolio.add_cash(margin + pnl - fee)
               self.ctx.store.add_trade([self.last_series.Index, "buy", size, self.last_series.close, notional, fee])
               self.ctx.store.add_ledger_record([self.last_series.Index, "realized_pnl", pnl, "USD"])
               self.ctx.store.add_ledger_record([self.last_series.Index, "commission", fee * -1, "USD"])

               if self.indicators is not None:
                  ind_values = {"datetime": self.last_series.Index}

                  for k, v in self.last_series[-len(self.indicators):].iteritems():
                     ind_values[k] = v

                  self.ctx.store.add_indicators_history(ind_values)

               if self.position.size > size:
                  self.position.size -= size
                  self.position.notional -= notional
                  self.position.margin -= margin
                  self.position.update_at = self.last_series.Index
               else:
                  self.position = None

               self.log("REDUCED POSITION - Side: BUY, Position Side: SHORT, Price: %f, Size: %f, Notional: %f, Fee: %f USD" % (
                   self.last_series.close, size, notional, fee * -1
               ))
            else:
               raise Exception("No opened positions to reduce size.")
         else:
            notional = self.last_series.close * size
            fee = notional * self.ctx.cfg.taker_fee_rate

            if self.position is not None:
               if self.position.side != "long":
                  raise Exception("Wrong side for opened position.")

               if leverage != self.position.leverage:
                  raise Exception("Wrong leverage for opened position.")

               margin = notional * (1 / self.position.leverage)

               if self.ctx.portfolio.cash < margin + fee:
                  raise Exception("Insufficient funds.")

               self.position.stop_price = stop_price
               self.position.size += size
               self.position.notional += notional
               self.position.margin += margin
               self.position.update_at = self.last_series.Index
               self.position.open_price = self.position.notional / self.position.size
               self.position.liquidation_price = self.get_liquidation_price(self.position.side, self.position.leverage, self.position.open_price)
               self.ctx.portfolio.sub_cash(margin + fee)
            else:
               margin = notional * (1 / leverage)

               if self.ctx.portfolio.cash < margin + fee:
                  raise Exception("Insufficient funds.")

               self.position = Position(
                   side="long",
                   leverage=leverage,
                   open_price=self.last_series.close,
                   stop_price=stop_price,
                   liquidation_price=self.get_liquidation_price("long", leverage, self.last_series.close),
                   size=size,
                   notional=notional,
                   margin=margin,
                   created_at=self.last_series.Index,
                   updated_at=self.last_series.Index
               )

            self.ctx.store.add_trade([self.last_series.Index, "buy", size, self.last_series.close, notional, fee])
            self.ctx.store.add_ledger_record([self.last_series.Index, "commission", fee * -1, "USD"])

            if self.indicators is not None:
               ind_values = {"datetime": self.last_series.Index}

               for k, v in self.last_series[-len(self.indicators):].iteritems():
                  ind_values[k] = v

               self.ctx.store.add_indicators_history(ind_values)

            self.log("NEW TRADE - Side: BUY, Price: %f, Size: %f, Notional: %f, Fee: %f USD" % (
                self.last_series.close, size, notional, fee * -1
            ))

      def sell(self, size: float, leverage: int = 1, stop_price: float = 0, take_profit_price: float = 0, reduce_only: bool = False):
         if size == 0:
            raise Exception("Size must be greater zero.")

         if reduce_only:
            if self.position is not None:
               if self.position.side != "long":
                  raise Exception("Wrong side for reduce only position.")

               pnl = (self.position.open_price - self.last_series.close) * size
               notional = self.last_series.close * size
               fee = notional * self.ctx.cfg.taker_fee_rate
               margin = notional * (1 / self.position.leverage)
               self.ctx.portfolio.add_cash(margin + pnl - fee)
               self.ctx.store.add_trade([self.last_series.Index, "sell", size, self.last_series.close, notional, fee])
               self.ctx.store.add_ledger_record([self.last_series.Index, "realized_pnl", pnl, "USD"])
               self.ctx.store.add_ledger_record([self.last_series.Index, "commission", fee * -1, "USD"])

               if self.indicators is not None:
                  ind_values = {"datetime": self.last_series.Index}

                  for k, v in self.last_series[-len(self.indicators):].iteritems():
                     ind_values[k] = v

                  self.ctx.store.add_indicators_history(ind_values)

               if self.position.size > size:
                  self.position.size -= size
                  self.position.notional -= notional
                  self.position.margin -= margin
                  self.position.update_at = self.last_series.Index
               else:
                  self.position = None

               self.log("REDUCED POSITION - Side: SELL, Position Side: LONG, Price: %f, Size: %f, Notional: %f, Fee: %f USD" % (
                   self.last_series.close, size, notional, fee * -1
               ))
            else:
               raise Exception("No opened positions to reduce size.")
         else:
            notional = self.last_series.close * size
            fee = notional * self.ctx.cfg.taker_fee_rate

            if self.position is not None:
               if self.position.side != "short":
                  raise Exception("Wrong side for opened position.")

               if leverage != self.position.leverage:
                  raise Exception("Wrong leverage for opened position.")

               margin = notional * (1 / self.position.leverage)

               if self.ctx.portfolio.cash < margin + fee:
                  raise Exception("Insufficient funds.")

               self.position.stop_price = stop_price
               self.position.size += size
               self.position.notional += notional
               self.position.margin += margin
               self.position.update_at = self.last_series.Index
               self.position.open_price = self.position.notional / self.position.size
               self.position.liquidation_price = self.get_liquidation_price(self.position.side, self.position.leverage, self.position.open_price)
               self.ctx.portfolio.sub_cash(margin + fee)
            else:
               margin = notional * (1 / leverage)

               if self.ctx.portfolio.cash < margin + fee:
                  raise Exception("Insufficient funds.")

               self.position = Position(
                   side="short",
                   leverage=leverage,
                   open_price=self.last_series.close,
                   stop_price=stop_price,
                   liquidation_price=self.get_liquidation_price("long", leverage, self.last_series.close),
                   size=size,
                   notional=notional,
                   margin=margin,
                   created_at=self.last_series.Index,
                   updated_at=self.last_series.Index
               )

            self.ctx.store.add_trade([self.last_series.Index, "sell", size, self.last_series.close, notional, fee])
            self.ctx.store.add_ledger_record([self.last_series.Index, "commission", fee * -1, "USD"])

            if self.indicators is not None:
               ind_values = {"datetime": self.last_series.Index}

               for k, v in self.last_series[-len(self.indicators):].iteritems():
                  ind_values[k] = v

               self.ctx.store.add_indicators_history(ind_values)

            self.log("NEW TRADE - Side: SELL, Price: %f, Size: %f, Notional: %f, Fee: %f USD" % (
                self.last_series.close, size, notional, fee * -1
            ))

      def close(self):
         if self.position is None:
            raise Exception("No opened positions to close.")

         if self.position.side == "long":
            pnl = (self.last_series.close - self.position.open_price) * self.position.size
            notional = self.last_series.close * self.position.size
            fee = notional * self.ctx.cfg.taker_fee_rate
            self.ctx.portfolio.add_cash(self.position.margin + pnl - fee)
            self.ctx.store.add_trade([self.last_series.Index, "sell", self.position.size, self.last_series.close, notional, fee])
            self.ctx.store.add_ledger_record([self.last_series.Index, "realized_pnl", pnl, "USD"])
            self.ctx.store.add_ledger_record([self.last_series.Index, "commission", fee * -1, "USD"])

            if self.indicators is not None:
               ind_values = {"datetime": self.last_series.Index}

               for k, v in self.last_series[-len(self.indicators):].iteritems():
                  ind_values[k] = v

               self.ctx.store.add_indicators_history(ind_values)

            self.position = None

            self.log("CLOSE POSITION - Side: SELL, Position Side: LONG, Price: %f, Size: %f, Notional: %f, Fee: %f USD" % (
                self.last_series.close, self.position.size, notional, fee * -1
            ))
         elif self.position.side == "short":
            pnl = (self.position.open_price - self.last_series.close) * self.position.size
            notional = self.last_series.close * self.position.size
            fee = notional * self.ctx.cfg.taker_fee_rate
            self.ctx.portfolio.add_cash(self.position.margin + pnl - fee)
            self.ctx.store.add_trade([self.last_series.Index, "buy", self.position.size, self.last_series.close, notional, fee])
            self.ctx.store.add_ledger_record([self.last_series.Index, "realized_pnl", pnl, "USD"])
            self.ctx.store.add_ledger_record([self.last_series.Index, "commission", fee * -1, "USD"])

            if self.indicators is not None:
               ind_values = {"datetime": self.last_series.Index}

               for k, v in self.last_series[-len(self.indicators):].iteritems():
                  ind_values[k] = v

               self.ctx.store.add_indicators_history(ind_values)

            self.position = None

            self.log("CLOSE POSITION - Side: BUY, Position Side: SHORT, Price: %f, Size: %f, Notional: %f, Fee: %f USD" % (
                self.last_series.close, self.position.size, notional, fee * -1
            ))

      def next(self):
         pass
