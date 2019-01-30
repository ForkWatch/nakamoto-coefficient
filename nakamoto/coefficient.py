import numpy as np
import pandas as pd


class SectorNakamoto(object):
    def __init__(self, data):
        self.data = data
        self.nakamoto_coefficient = self.generate_nakamoto_coefficient()
    
    def generate_nakamoto_coefficient(self):
        cutoff = 0.51
        nakamoto_test = self.data > cutoff 
        nakamoto = sum(nakamoto_test)
        return nakamoto

    def get_nakamoto_coefficient(self):
        if self.nakamoto_coefficient:
            return self.nakamoto_coefficient


class Nakamoto(object):
    def __init__(self, nakamoto_list):
        self.nakamoto_dict = {}
        self.gini_dict = {}
        self.nakamoto_list = nakamoto_list
        self.minimum_nakamoto_id = None
        self.maximum_gini_id = None
        for nakamoto_obj in self.nakamoto_list:
            self.nakamoto_dict[nakamoto_obj.type] = nakamoto_obj.get_nakamoto_coefficient()
            self.gini_dict[nakamoto_obj.type] = nakamoto_obj.get_gini_coefficient()
        self.minimum_nakamoto = None 
        self.maximum_gini = None

    def generate_minimum_nakamoto(self):
        self.minimum_nakamoto_id = min(self.nakamoto_dict, key=self.nakamoto_dict.get)
        minimum_nakamoto_value = self.nakamoto_dict[self.minimum_nakamoto_id]
        return minimum_nakamoto_value

    def generate_maximum_gini(self):
        self.maximum_gini_id = max(self.gini_dict, key=self.gini_dict.get)
        maximum_gini_value = self.gini_dict[self.maximum_gini_id]
        return maximum_gini_value

    def get_minimum_nakamoto(self):
        if not self.minimum_nakamoto:
            self.minimum_nakamoto = self.generate_minimum_nakamoto()
        return self.minimum_nakamoto

    def get_maximum_gini(self):
        if not self.maximum_gini:
            self.maximum_gini = self.generate_maximum_gini()
        return self.maximum_gini

    def get_minimum_nakamoto_id(self):
        if not self.minimum_nakamoto_id:
            _ = self.generate_minimum_nakamoto()
        return self.minimum_nakamoto_id

    def get_maximum_gini_id(self):
        if not self.maximum_gini_id:
            _ = self.generate_maximum_gini()
        return self.maximum_gini_id
    
    def get_sector_series(self, sector):
        data_labels = ['Gini Coefficient', 'Nakamoto Coefficient']
        data = [round(sector.get_gini_coefficient(), 3), 
                sector.get_nakamoto_coefficient()]
        series = pd.Series(data, index=data_labels, name=sector.type)
        return series

    def get_summary(self):
        sector_series = []
        for sector in self.nakamoto_list:
            series = self.get_sector_series(sector)
            sector_series.append(series)
        nakamoto_dataframe = pd.concat(sector_series, axis=1)
        return nakamoto_dataframe.transpose()
