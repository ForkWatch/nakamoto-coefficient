class Nakamoto(object):
    def __init__(self, sector):
        self.currency = sector.currency
        self.gini = sector.gini
        self.data = sector.data
        self.id = sector.id
        self.nakamoto = self.get_nakamoto_coefficient()
    
    def generate_nakamoto_coefficient(self):
        nakamoto_test = self.data > 0.51
        nakamoto = sum(nakamoto_test)
        return nakamoto

    def get_nakamoto_coefficient(self):
        if self.nakamoto:
            return self.nakamoto


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
