# import pandas as pd
# import numpy as np
# import requests
# import math
# import matplotlib.pyplot as plt
# from alpha_vantage.timeseries import TimeSeries
# from alpha_vantage.fundamentaldata import FundamentalData

# import time

# api_key = 'T6VFDMV26J1LQK5K'

# renewable_energy_stonks = ['AAPL']

# ts = TimeSeries(key=api_key, output_format='pandas')
# fd = FundamentalData(key=api_key, output_format='pandas')

# for stock in renewable_energy_stonks:
#     data, meta_data = ts.get_intraday(symbol=f'{stock}',interval='1min', outputsize='full')
#     data['4. close'].plot()
#     plt.show()
#     # data_fd = fd.get_cash_flow_quarterly(renewable_energy_stonks)
#     # print(data[0])
#     # close_data = data['4. close']
#     # change = close_data.pct_change()
#     # print(change[1])
#     # plt.plot(change)
#     # plt.show()
#     # time.sleep(60)



