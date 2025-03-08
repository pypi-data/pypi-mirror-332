import pandas as pd



class Insiders:
    def __init__(self, data):


        self.name = [i.get('name') for i in data]
        self.transaction_date = [i.get('transaction_date') for i in data]
        self.shares = [float(i.get('shares')) for i in data]


        self.data_dict = { 
            'name': self.name,
            'transaction_date': self.transaction_date,
            'shares': self.shares
        }


        self.df = pd.DataFrame(self.data_dict)


        