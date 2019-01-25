from .sector import Sector
from .analysis import Gini, LorenzPlot
from nakamoto import SectorNakamoto
from requests_html import HTMLSession
import pandas as pd
import numpy as np


class Market(Sector):
    def __init__(self, currency, market_url, **kwargs):
        super(Market, self).__init__(currency, **kwargs)
        self.market_url = market_url
        self.generate_market_data()
        
    def generate_market_data(self):
        session = HTMLSession()
        r = session.get(self.market_url)
        table = r.html.find('#markets-table', first=True)
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
        gini_object = Gini(self.data)
        self.gini = gini_object.get_gini()
        self.plot = self.generate_lorenz_curve()
        self.nakamoto = self.generate_nakamoto_coefficient()

    def generate_nakamoto_coefficient(self):
        nakamoto_object = SectorNakamoto(self.lorenz_data)
        nakamoto = nakamoto_object.get_nakamoto_coefficient()
        return nakamoto

    def generate_lorenz_curve(self):
        file_name = f'{self.currency}_exchanges_gini_{self.uuid}'
        lorenz_object = LorenzPlot(self.plotly_username, self.plotly_api_key, self.data, file_name)
        plot_url = lorenz_object.get_plot_url()
        self.lorenz_data = lorenz_object.get_lorenz_data()
        return plot_url
