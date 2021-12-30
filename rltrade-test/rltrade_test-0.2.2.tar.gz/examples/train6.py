import asyncio
from rltrade import config
from metaapi_cloud_sdk import MetaApi
from rltrade.backtests import get_metrics
from rltrade.data import OandaDownloader
from rltrade.models import SmartTradeAgent


"""
time_frame - last date available
1d - (2018-01-07)
"""

time_frame = "1d" #keep is 1d in this file or else it won't work
train_period = ('2012-08-04','2021-01-01') #for training the model
test_period = ('2021-01-02','2021-12-20') #for testing the model
start_time = "17:00:00"
end_time = "23:55:00" #does not matter in daily trading.
path = 'models/dailytrade/forex-CADCHF'

token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIzYTI0YzMwYzFkNDRmZGFmZGI3NmVmYTUxZmQ2MDJmMCIsInBlcm1pc3Npb25zIjpbXSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaWF0IjoxNjM5NDkwMzEzLCJyZWFsVXNlcklkIjoiM2EyNGMzMGMxZDQ0ZmRhZmRiNzZlZmE1MWZkNjAyZjAifQ.DhA6Q-AlWNssi8ScOaWy2Bxo4Hebgw94BDE6PiT9J-TvsuF7OqvdYBQ1IWYEMtsYsg3Ij8p8Wpvn8ZdZeHRkR3vLcQnMH-GZj3DyYkeqovQKk6U3uOobV-GS3meJPZYfw2zItuTDBWxuHDZsVW1ZvF4sItBDmsWIe2svF0NmKE1nu-ephcYVzYo9grr93de_h-QwlP-yeZFeGEqrz3-q5gYWcARJsIR1BX63zePuDHkUK9k5W9Rm28WdB87MHEyMSWhcAZDf8si5MwsPYC3wpzNtzGqORF3UY-w5EmolCtSPMBqM7AI0LKc1n8GPS3ZhnvHkfGhWEdb5gKlCWwshk30tICN24C1bZG06zfs450oLm8ih9ls5oyshcg_xwawNvsA305D7Siz0Pzqr1xnUA8zMz8cVUFZtjdBWCfot05_ziVO0x_mApVyAVC2OA-Sh61RtkwNNpg4bTCzK30OpdiS9GO0HLgnepnuwWOO0T9DTzTAJUxyJcXOzcWcXGdMTWaGAp5ranytU97k8GxDHa5jOS_WvphL24C8QA6of0pYZwHM3Ul5Aw351H1SbJLIqs2AChDoUnpJb9OZb-27ESLZgM1mhU6rwzt8lRRbxUHaXSv5QpM29nPm3k5KrFSv-UTXiX6oU9c1nNh3qLb6FKV_B1CQarcvyx66iUg-1DcU'
domain = 'agiliumtrade.agiliumtrade.ai'
account_id = 'ddc8fb93-e0f5-4ce8-b5d5-8290d23fc143'

# ticker_list = ['AUDUSD','EURUSD','NZDUSD','USDCAD','USDCHF','GBPUSD']
ticker_list = ['USDCAD','USDCHF']
sec_types = ['-'] * len(ticker_list)
exchanges = ['-'] * len(ticker_list)

#CADCHF - 3 epochs
#EURGBP - 2 epochs
#AUDNZD - 2 epochs

# tech_indicators = config.STOCK_INDICATORS_LIST # indicators from stockstats
# additional_indicators = config.ADDITIONAL_STOCK_INDICATORS

tech_indicators = [
    "macd",
    "boll_ub",
    "boll_lb",
    "rsi_30",
    "dx_30",
    "close_30_sma",
    "close_60_sma",
    "kdjk",
    "open_2_sma",
    "boll",
    "close_10.0_le_5_c",
    "wr_10",
	"dma",
    "trix",
	"vr_6_sma",
	"vr",
	"close_2_tema",
	"tema",
	"trix_9_sma",
	"close_3_trix",
	"adxr",
	"adx",
	"dx",
	"mdi",
	"pdi",
	"atr",
	"tr",
	"cci_20",
	"cci",
	"wr_6",
	"rsi_12",
	"rsi_6",
	"cr-ma2_xu_cr-ma1_20_c",
	"macdh",
	"macds",
	"kdjj",
	"kdjd",
	"volume_-3~1_min",
	"volume_-3,2,-1_max",
	"cr-ma3",
	"cr-ma2",
	"cr-ma1",
	"cr",
	"open_-2_r",
	"open_2_d",
	"volume_delta"
]

additional_indicators = [
    # 'vpin_5',
    # 'vpin_22',
    # 'vpin_66',
    # 'vpin_1year',
    # 'vpin_3year',
    # 'vpin_5year',

    'price_diff_5',
    'price_diff_22',
    'price_diff_66',
    'price_diff_1year',
    'price_diff_3year',
    'price_diff_5year',

    'sharpe_diff_5',
    'sharpe_diff_22',
    'sharpe_diff_66',
    'sharpe_diff_1year',
    'sharpe_diff_3year',
    'sharpe_diff_5year',

    'sortino_diff_5',
    'sortino_diff_22',
    'sortino_diff_66',
    'sortino_diff_1year',
    'sortino_diff_3year',
    'sortino_diff_5year',

    'calamar_diff_5',
    'calamar_diff_22',
    'calamar_diff_66',
    'calamar_diff_1year',
    'calamar_diff_3year',
    'calamar_diff_5year',

    'vix_fix_diff_5',
    'vix_fix_diff_22',
    'vix_fix_diff_66',
    'vix_fix_diff_1year',
    'vix_fix_diff_3year',
    'vix_fix_diff_5year',

    'max_value_price_diff_5',
    'max_value_price_diff_22',
    'max_value_price_diff_66',
    'max_value_price_diff_1year',
    'max_value_price_diff_3year',
    'max_value_price_diff_5year',

    'min_value_price_diff_5',
    'min_value_price_diff_22',
    'min_value_price_diff_66',
    'min_value_price_diff_1year',
    'min_value_price_diff_3year',
    'min_value_price_diff_5year',

    'max_value_volume_diff_5',
    'max_value_volume_diff_22',
    'max_value_volume_diff_66',
    'max_value_volume_diff_1year',
    'max_value_volume_diff_3year',
    'max_value_volume_diff_5year',

    'min_value_volume_diff_5',
    'min_value_volume_diff_22',
    'min_value_volume_diff_66',
    'min_value_volume_diff_1year',
    'min_value_volume_diff_3year',
    'min_value_volume_diff_5year',

    'sharpe_5',
    'sharpe_22',
    'sharpe_66',
    'sharpe_1year',
    'sharpe_3year',
    'sharpe_5year',

    'sortino_5',
    'sortino_22',
    'sortino_66',
    'sortino_1year',
    'sortino_3year',
    'sortino_5year',

    'calamar_5',
    'calamar_22',
    'calamar_66',
    'calamar_1year',
    'calamar_3year',
    'calamar_5year',

    'vix_fix_5',
    'vix_fix_22',
    'vix_fix_66',
    'vix_fix_1year',
    'vix_fix_3year',
    'vix_fix_5year',

    'max_value_price_5',
    'max_value_price_22',
    'max_value_price_66',
    'max_value_price_1year',
    'max_value_price_3year',
    'max_value_price_5year',

    'min_value_price_5',
    'min_value_price_22',
    'min_value_price_66',
    'min_value_price_1year',
    'min_value_price_3year',
    'min_value_price_5year',

    'max_value_volume_5',
    'max_value_volume_22',
    'max_value_volume_66',
    'max_value_volume_1year',
    'max_value_volume_3year',
    'max_value_volume_5year',

    'min_value_volume_5',
    'min_value_volume_22',
    'min_value_volume_66',
    'min_value_volume_1year',
    'min_value_volume_3year',
    'min_value_volume_5year',

    'hurst_exp'
]

env_kwargs = {
    "initial_amount": 17500, #this does not matter as we are making decision for lots and not money.
    "ticker_col_name":"tic",
    "stop_loss":0.015,
    "filter_threshold":1, #between 0.1 to 1, select percentage of top stocks 0.3 means 30% of top stocks
    "target_metrics":['asset'], #asset, cagr, sortino, calamar, skew and kurtosis are available options.
    "transaction_cost":0, #transaction cost per order
    "tech_indicator_list":tech_indicators + additional_indicators, 
    "reward_scaling": 1}

PPO_PARAMS = {'ent_coef':0.005,
            'learning_rate':0.01,
            'batch_size':252}

async def train_model():
    api = MetaApi(token,{'domain':domain})

    try:
        account = await api.metatrader_account_api.get_account(account_id)

        if account.state != 'DEPLOYED':
            print("Deploying account")
            await account.deploy()
        else:
            print('Account already deployed')
        if account.connection_status != 'CONNECTED':
            print('Waiting for API server to connect to broker (may take couple of minutes)')
            await account.wait_connected()
        else:
            print("Account already connected")
    
        oa = OandaDownloader(
            account = account,
            time_frame=time_frame,
            start_date=train_period[0],
            end_date=test_period[1],
            start_time=start_time,
            end_time=end_time,
            ticker_list=ticker_list)

        df = await oa.fetch_daily_data()

        agent = SmartTradeAgent("ppo",
                            df=df,
                            account=account,
                            time_frame=time_frame,
                            ticker_list=ticker_list,
                            sec_types = sec_types,
                            exchanges=exchanges,
                            ticker_col_name="tic",
                            tech_indicators=tech_indicators,
                            additional_indicators=additional_indicators,
                            train_period=train_period,
                            test_period=test_period,
                            start_time=start_time,
                            end_time=end_time,
                            env_kwargs=env_kwargs,
                            model_kwargs=PPO_PARAMS,
                            tb_log_name='ppo',
                            epochs=10)

        agent.train_model()
        agent.save_model(path) #save the model for trading

        df_daily_return,df_actions = agent.make_prediction() #testing model on testing period
        get_metrics(path)

    except Exception as err:
        print(api.format_error(err))


asyncio.run(train_model())