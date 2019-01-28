from .sector import Sector
from requests_html import HTMLSession
import pandas as pd
import numpy as np


class Market(Sector):
    def __init__(self, currency, market_url, **kwargs):
        super(Market, self).__init__(currency, **kwargs)
        self.type = 'market'
        self.market_url = market_url
        self.generate_market_data()
        
    def generate_market_data(self):
        session = HTMLSession()
        r = session.get(self.market_url)
        table = r.html.find('#markets-table', first=True)
        session.close()
        market_df = pd.read_html(table.html)[0]
        volume_data = market_df['Volume (24h)']
        volume_data = volume_data.str.replace('$', '', regex=False)
        volume_data = volume_data.str.replace('*** ', '', regex=False)
        volume_data = volume_data.str.replace('** ', '', regex=False)
        volume_data = volume_data.str.replace('* ', '', regex=False)
        volume_data = volume_data.str.replace(',', '', regex=False)
        volume_data = pd.to_numeric(volume_data)
        volume_data = volume_data.sort_values()
        self.data = np.array(volume_data)
