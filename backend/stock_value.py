import requests

class StockValue():
    def __init__(self, stockNameThis, stockNameOther):
        self.apiKey = 'T6VFDMV26J1LQK5K'
        self.stockNameThis = stockNameThis
        self.stockNameOther = stockNameOther
    
    def compareStocks(self):
        dataStockThis = requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'.format(self.stockNameThis, self.apiKey))
        dataStockOther = requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'.format(self.stockNameOther, self.apiKey))
        
        PERatioThis = float(dataStockThis.json()['PERatio'])
        PBRatioThis = float(dataStockThis.json()['PriceToBookRatio'])
        EVtoEBITDAThis = float(dataStockThis.json()['EVToEBITDA'])
        PSRatioThis = float(dataStockThis.json()['PriceToSalesRatioTTM'])

        PERatioOther = float(dataStockOther.json()['PERatio'])
        PBRatioOther = float(dataStockOther.json()['PriceToBookRatio'])
        EVtoEBITDAOther = float(dataStockOther.json()['EVToEBITDA'])
        PSRatioOther = float(dataStockOther.json()['PriceToSalesRatioTTM'])

        meanThis = (PERatioThis + PBRatioThis + EVtoEBITDAThis + PSRatioThis)/4
        meanOther = (PERatioOther + PBRatioOther + EVtoEBITDAOther + PSRatioOther)/4

        if (meanThis > meanOther):
            return (self.stockNameThis, PERatioThis, PBRatioThis, EVtoEBITDAThis, PSRatioThis)
        else:
            return (self.stockNameOther, PERatioOther, PBRatioOther, EVtoEBITDAOther, PSRatioOther)
        

        





# if __name__ == '__main__':
#     val = StockValue('IBM', "AAPL")
#     data = val.compareStocks()
#     print(data)
    














# import requests

# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=T6VFDMV26J1LQK5K'
# r = requests.get(url)
# data = r.json()
# print(type(data))
# print(data)