from alpha_vantage.timeseries import TimeSeries


class StockDisplay():
    def __init__(self, stockName, timePeriod):
        self.apiKey = 'T6VFDMV26J1LQK5K'
        self.stockName = stockName
        self.timePeriod = timePeriod
    
    def stockData(self):
        ts = TimeSeries(key=self.apiKey, output_format='pandas')
        if (self.timePeriod == "interday"):
            data, meta_data = ts.get_intraday(symbol=self.stockName)
        elif (self.timePeriod == "daily"):
            data, meta_data = ts.get_daily(symbol=self.stockName)
        elif (self.timePeriod == "weekly"):
            data, meta_data = ts.get_weekly(symbol=self.stockName)
        elif (self.timePeriod == "monthly"):
            data, meta_data = ts.get_monthly(symbol=self.stockName)
        
        return data
    



# if __name__ == '__main__':
#     sl = StockLogic('AAPL', "daily", "sma")
#     data = sl.stockData()
#     print(data)
#     idata, datasma = sl.stockIndicators()
#     print(idata)
#     print(datasma)
