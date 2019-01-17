from .analysis import Gini, LorenzPlot
from nakamoto import Nakamoto
import uuid

class Sector(object):
    def __init__(self, data, currency, plotly_username, plotly_api_key):
        self.uuid = uuid.uuid4()
        self.data = data
        self.plotly_username = plotly_username
        self.plotly_api_key = plotly_api_key
        self.currency = currency
        self.nakamoto = None
        self.plot = None
        self.title = None
        self.gini = None

    def get_gini_coefficient(self):
        if self.gini:
            return self.gini

    def get_plot_url(self):
        if self.plot:
            return self.plot

    def get_nakamoto_coefficient(self):
        if self.nakamoto:
            return self.nakamoto

class CustomSector(object):
    def __init__(self, data, currency, sector_type):
        self.uuid = uuid.uuid4()
        self.data = data
        self.gini = self.generate_gini()
        self.currency = currency
        self.type = sector_type
        self.plot = self.generate_plot_url()
        self.nakamoto = self.generate_nakamoto()

    def generate_gini(self):
        gini_object = Gini(self.data)
        gini = gini_object.get_gini()
        return gini

    def generate_plot_url(self):
        file_name = f'{self.currency}_{self.type}_gini_{self.uuid}'
        lorenz_object = LorenzPlot(self.plotly_username, self.plotly_api, self.contributor_data, file_name)
        plot_url = lorenz_object.plotly_url()
        return plot_url

    def generate_nakamoto(self):
        nakamoto_object = Nakamoto(self.data)
        nakamoto = nakamoto_object.get_nakamoto_coefficient()
