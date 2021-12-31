import backtrader as bt


class BuyAndHold(bt.Backtrader.Strategy):
   def __init__(self, ctx):
      super().__init__(ctx)
      self.name = "Buy & Hold"
      self.min_trade_notional = 100

   def next(self):
      if self.last_series.Index.weekday() == 0 and self.last_series.Index.hour == 0 and self.last_series.Index.minute == 0:
         if self.ctx.portfolio.cash < self.min_trade_notional:
            self.min_trade_notional = self.ctx.portfolio.cash

         fee = self.min_trade_notional * self.ctx.cfg.taker_fee_rate

         if self.ctx.portfolio.cash >= self.min_trade_notional + fee:
            size = self.min_trade_notional / self.last_series.close
            self.buy(size=size)


ohlc_data = bt.OHLCData(
    symbol="BTC/USD",
    files=[
           "/Users/pol.maksim/Google Drive/Мой диск/OHLC Data/bitfinex-BTC-USD-1m.csv"
    ],
    timestamp=0,
    datetime=-1,
    open=1,
    high=3,
    low=4,
    close=2,
    volume=5,
    timeframe="1m",
    compression="5m",
    dtformat="%Y-%m-%d %H:%M:%S",
    tsformat="ms",
    separator=",",
    header=0,
    ascending=True
)


if __name__ == "__main__":
   b = bt.Backtrader()
   b.set_taker_fee_rate(0.04)
   b.set_funding_rate(0.01)
   b.set_funding_rate_interval(28800)
   b.set_decimals(2)
   b.add_ohlc_data(ohlc_data)
   b.debug_mode(False)
   b.set_cash(100000)
   b.set_strategy(BuyAndHold)

   report = b.run()
   report.info()
