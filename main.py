import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'T6VFDMV26J1LQK5K'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
print(data)

close_data = data['4. close']
