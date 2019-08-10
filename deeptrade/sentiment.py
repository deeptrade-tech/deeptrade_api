import request
import stripe
import pandas as pd

class Sentiment():

    def __init__(self):

        self.head = {'Authorization': "Token %s" %stripe.api_key}

    def by_date(self,date,dataframe=False):
        """
        :parameters:
        - date: a day date in the format %YYYY-%MM-%DD
        - dataframe: whehter result in json (False) or pandas dataframe
        
        :returns:
        json or pandas dataframe with all the ticker of the day date and 
        their corresponding sentiment
        """
        endpoint = stripe.api_base+"sentiment_get/"+date
        g = requests.get(endpoint, headers=self.head).json()
        if dataframe:
            df = pd.DataFrame(g)
            return df
        else:
            return g
        
            
            
        
        
