import numpy as np

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

class MinimumNakamoto(object):
    def __init__(self, nakamoto_list):
        self.nakamoto_dict = {}
        self.nakamoto_list = nakamoto_list
        self.minimum_coefficient_sector_id = None
        for nakamoto_obj in self.nakamoto_list:
            self.nakamoto_dict[nakamoto_obj.id] = nakamoto_obj.get_nakamoto_coefficient()
        self.minimum_coefficient = self.generate_minimum_nakamoto()

    def generate_minimum_nakamoto(self):
        self.minimum_coefficient_sector_id = min(self.nakamoto_dict, key=self.nakamoto_dict.get)
        minimum_coefficient_nakamoto_value = self.nakamoto_dict[self.minimum_coefficient_sector_id]
        return minimum_coefficient_nakamoto_value

    def get_minimum_nakamoto(self):
        if self.minimum_coefficient:
            return self.minimum_coefficient

    def get_mininum_nakamoto_id(self):
        if self.minimum_coefficient_sector_id:
            return self.minimum_coefficient_sector_id
