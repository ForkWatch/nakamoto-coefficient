from .analysis import Gini, LorenzPlot
from nakamoto.coefficient import SectorNakamoto
import uuid
import numpy as np


class Sector(object):
    def __init__(self, currency, **kwargs):
        self.uuid = uuid.uuid4()
        self.data = None 
        self.type = None
        self.plotly_username = kwargs.get('plotly_username')
        self.plotly_api_key = kwargs.get('plotly_api_key')
        self.currency = currency
        self.lorenz_data = None
        self.lorenz_object = None
        self.nakamoto = None
        self.plot = None
        self.title = None
        self.gini = None

    def generate_gini_coefficient(self):
        if self.data is not None:
            gini_object = Gini(self.data)
            gini = gini_object.get_gini()
            return gini
        else:
            raise Exception('Cannot generate gini. No data')
    
    def generate_nakamoto_coefficient(self):
        if not self.lorenz_data:
            self.lorenz_data = self.generate_lorenz_data()
        nakamoto_object = SectorNakamoto(self.lorenz_data)
        nakamoto = nakamoto_object.get_nakamoto_coefficient()
        return nakamoto

    def generate_lorenz_object(self):
        file_name = f'{self.currency}_{self.type}_gini_{self.uuid}'
        title_name = f'{self.currency} {self.type.capitalize()} Lorenz Curve'
        lorenz_object = LorenzPlot(self.plotly_username, self.plotly_api_key, self.data, file_name, title_name)
        return lorenz_object

    def generate_lorenz_data(self):
        if not self.lorenz_object:
            self.lorenz_object = self.generate_lorenz_object()
        lorenz_data = self.lorenz_object.get_lorenz_data()
        return lorenz_data

    def generate_lorenz_curve(self):
        if not self.lorenz_object:
            self.lorenz_object = self.generate_lorenz_object()
        plot_url = self.lorenz_object.get_plot_url()
        return plot_url

    def get_lorenz_data(self):
        if not self.lorenz_data:
            self.lorenz_data = self.generate_lorenz_data()
        return self.lorenz_data

    def get_gini_coefficient(self):
        if not self.gini:
            self.gini = self.generate_gini_coefficient()
        return self.gini

    def get_plot_url(self):
        if not self.plot:
            self.plot = self.generate_lorenz_curve()
        return self.plot

    def get_nakamoto_coefficient(self):
        if not self.nakamoto:
            self.nakamoto = self.generate_nakamoto_coefficient()
        return self.nakamoto

    
class CustomSector(object):
    def __init__(self, data, currency, sector_type, **kwargs):
        self.uuid = uuid.uuid4()
        self.data = data
        if type(self.data) is not np.ndarray:
            raise Exception('Sector data must be a numpy array')
        if len(self.data) == 0:
            raise Exception('Cannot pass empty data numpy array')
        self.plotly_username = kwargs.get('plotly_username')
        self.plotly_api_key = kwargs.get('plotly_api_key')
        self.gini = None 
        self.currency = currency
        self.type = sector_type
        self.plot = None 
        self.nakamoto = None 
        self.lorenz_data = None
        self.lorenz_object = None

    def generate_gini_coefficient(self):
        if self.data is not None:
            gini_object = Gini(self.data)
            gini = gini_object.get_gini()
            return gini
        else:
            raise Exception('Cannot generate gini. No data')
    
    def generate_nakamoto_coefficient(self):
        if not self.lorenz_data:
            self.lorenz_data = self.generate_lorenz_data()
        nakamoto_object = SectorNakamoto(self.lorenz_data)
        nakamoto = nakamoto_object.get_nakamoto_coefficient()
        return nakamoto

    def generate_lorenz_object(self):
        file_name = f'{self.currency}_{self.type}_gini_{self.uuid}'
        title_name = f'{self.currency} {self.type.capitalize()} Lorenz Curve'
        lorenz_object = LorenzPlot(self.plotly_username, self.plotly_api_key, self.data, file_name, title_name)
        return lorenz_object

    def generate_lorenz_data(self):
        if not self.lorenz_object:
            self.lorenz_object = self.generate_lorenz_object()
        lorenz_data = self.lorenz_object.get_lorenz_data()
        return lorenz_data

    def generate_lorenz_curve(self):
        if not self.lorenz_object:
            self.lorenz_object = self.generate_lorenz_object()
        plot_url = self.lorenz_object.get_plot_url()
        return plot_url

    def get_lorenz_data(self):
        if not self.lorenz_data:
            self.lorenz_data = self.generate_lorenz_data()
        return self.lorenz_data

    def get_gini_coefficient(self):
        if not self.gini:
            self.gini = self.generate_gini_coefficient()
        return self.gini

    def get_plot_url(self):
        if not self.plot:
            self.plot = self.generate_lorenz_curve()
        return self.plot

    def get_nakamoto_coefficient(self):
        if not self.nakamoto:
            self.nakamoto = self.generate_nakamoto_coefficient()
        return self.nakamoto

