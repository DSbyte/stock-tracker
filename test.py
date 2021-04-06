# import pandas as pd
# import matplotlib.pyplot as plt
# import alpha_vantage.timeseries as TimeSeries
# import alpha_vantage.techindicators as TechIndicators

# ts = TimeSeries(key=self.api_key, output_format='pandas')
# ts.

# class Indicators:
#     def __init__(self, stock_name, time_period):
#         self.api_key = 'T6VFDMV26J1LQK5K'
#         self.stock = stock_name
#         self.time = time_period

#     def close_price(self):
        
        
#         if (self.time == 'interday'):
#             ts = TimeSeries(key=self.api_key, output_format='pandas')
#             data, meta_data = ts.get_intraday(symbol=f'{self.stock}',interval='15min', outputsize='full')
#         elif (self.time == 'daily'):
#             tss = TimeSeries(key=self.api_key, output_format='pandas')
#             data, meta_data = tss.get_daily(symbol=f'{self.stock}',interval='15min', outputsize='full')
#         elif (self.time == 'weekly'):
#             ts = TimeSeries(key=self.api_key, output_format='pandas')
#             data, meta_data = ts.get_weekly(symbol=f'{self.stock}',interval='15min', outputsize='full')
#         elif (self.time == 'monthly'):
#             ts = TimeSeries(key=self.api_key, output_format='pandas')
#             data, meta_data = ts.get_monthly(symbol=f'{self.stock}',interval='15min', outputsize='full')

#         return data

#     def sma(self):
#         ti = TechIndicators(key=self.api_key, output_format='pandas')
#         data, meta_data = ti.get_sma(symbol=self.stock, time_period=30)
        
#         return data

#     def display(self):
#         close = self.close_price()
#         plt.plot(close['4. close'])
        
#         sma = self.sma()
#         print(sma)

#         plt.show()

# if __name__ == "__main__":
#     i = Indicators('AAPL', 'weekly')
#     i.display()