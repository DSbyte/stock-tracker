from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

class StockIndicators():
    def __init__(self, stockName, timePeriod, stockIndi):
        self.apiKey = 'T6VFDMV26J1LQK5K'
        self.stockName = stockName
        self.timePeriod = timePeriod
        self.stockIndi = stockIndi

    def stockIndicators(self):
        ti = TechIndicators(key=self.apiKey, output_format='pandas')

        ts = TimeSeries(key=self.apiKey, output_format='pandas')
        data, meta_data = ts.get_monthly(symbol=self.stockName)
        dataIndi, meta_dataIndi = ti.get_sma(symbol=self.stockName, time_period=30)

        if (self.stockIndi == "ema"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_ema(symbol=self.stockName, time_period=30)
        
        elif (self.stockIndi == "vwap"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_vwap(symbol=self.stockName, time_period=30)
        
        elif (self.stockIndi == "macd"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_macd(symbol=self.stockName, time_period=30)
        
        elif (self.stockIndi == "obv"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_obv(symbol=self.stockName, time_period=30)

        elif (self.stockIndi == "ad"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_ad(symbol=self.stockName, time_period=30)

        elif (self.stockIndi == "bbands"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_bbands(symbol=self.stockName, time_period=30)
        
        elif (self.stockIndi == "aroon"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_aroon(symbol=self.stockName, time_period=30)
        
        elif (self.stockIndi == "cci"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_cci(symbol=self.stockName, time_period=30)
        
        elif (self.stockIndi == "adx"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_adx(symbol=self.stockName, time_period=30)
        
        elif (self.stockIndi == "rsi"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_rsi(symbol=self.stockName, time_period=30)
        
        elif (self.stockIndi == "stoch"):
            ts = TimeSeries(key=self.apiKey, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=self.stockName)
            dataIndi, meta_dataIndi = ti.get_stoch(symbol=self.stockName, time_period=30)
        

        return data, dataIndi