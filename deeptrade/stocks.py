import requests
import deeptrade
import pandas as pd

class StockPrice():

    def __init__(self):

        self.head = {'Authorization': "Token %s" %deeptrade.api_key}

    def by_date(self,date,dataframe=False):
        """
        :parameters:
        - date: a day date in the format %YYYY-%MM-%DD
        - dataframe: whehter result in json (False) or pandas dataframe
        
        :returns:
        json or pandas dataframe with all the tickers of the day date and 
        their corresponding stock price (OHLC)
        """
        endpoint = deeptrade.api_base+"stock_date/"+date
        g = requests.get(endpoint, headers=self.head).json()
        if dataframe:
            df = pd.DataFrame(g)
            return df
        else:
            return g

        
    def by_ticker(self,ticker,dataframe=False):
        """
        :parameters:
        - ticker: a ticker such as 'AMZN'
        - dataframe: whehter result in json (False) or pandas dataframe
        
        :returns:
        json or pandas dataframe with all the hist. OHLC information of the ticker
        """
        endpoint = deeptrade.api_base+"stocks/"+ticker
        g = requests.get(endpoint, headers=self.head).json()
        if dataframe:
            df = pd.DataFrame(g)
            return df
        else:
            return g


    def stock_by_date_ticker(self, date, ticker,  dataframe=False):
        """
        :parameters:
        - ticker: a day date in the format %YYYY-%MM-%DD
        - dataframe: whehter result in json (False) or pandas dataframe
        
        :returns:
        json or pandas dataframe with all the hist. OHLC & stock information for the particular date
        """
        endpoint = deeptrade.api_base+"stockdate/"+ticker+'/'+date
        g = requests.get(endpoint, headers=self.head).json()
        if dataframe:
            df = pd.DataFrame(g)
            return df
        else:
            return g


    
