import unittest
from nakamoto import SectorNakamoto, Nakamoto
from nakamoto.sector import CustomSector, Client, Geography, Market, Repository
import numpy as np
import pandas as pd
import os
import warnings
import logging


random_data = np.append(np.random.poisson(lam=10, size=40), 
                 np.random.poisson(lam=100, size=10))

random_data_2 = np.append(np.random.poisson(lam=10, size=40), 
                 np.random.poisson(lam=100, size=10))

currency = 'ETC'
market_url = 'https://coinmarketcap.com/currencies/ethereum-classic/#markets'

nakamoto_config = {
    'plot_notebook': os.environ['PLOT_NOTEBOOK'],
    'plot_image_path': os.environ['PLOT_IMAGE_PATH']
}

github_url = 'https://github.com/input-output-hk/mantis'
github_api = os.environ['GITHUB_API']



class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client(currency, **nakamoto_config)

    def test_client_gini(self):
        gini = self.client.get_gini_coefficient()
        gini_range = (gini < 1.0) and (gini > 0.0)
        self.assertTrue(gini_range, 'Client Gini Not In Correct Range')

    def test_client_nakamoto(self):
        nakamoto = self.client.get_nakamoto_coefficient()
        nakamoto_range = nakamoto > 0
        self.assertTrue(nakamoto_range, 'Nakamoto Coefficient is Zero')

    def test_client_plot(self):
        self.client.get_plot()
        image_path = nakamoto_config['plot_image_path']
        image_exists = os.path.isfile(image_path)
        #self.assertTrue(image_exists)


class TestGeography(unittest.TestCase):
    def setUp(self):
        self.geography = Geography(currency, **nakamoto_config)
        
    def test_geography_gini(self):
        gini = self.geography.get_gini_coefficient()
        gini_range = (gini < 1.0) and (gini > 0.0)
        self.assertTrue(gini_range, 'Geography Gini Not In Correct Range')

    def test_geography_nakamoto(self):
        nakamoto = self.geography.get_nakamoto_coefficient()
        nakamoto_range = nakamoto > 0
        self.assertTrue(nakamoto_range, 'Nakamoto Coefficient is Zero')

    def test_geography_plot(self):
        plot = self.geography.get_plot()
        self.assertNotEqual(plot, '', 'Empty Url String Returned')


class TestMarket(unittest.TestCase):
    def setUp(self):
        self.market = Market(currency, market_url, **nakamoto_config)
        
    def test_market_gini(self):
        gini = self.market.get_gini_coefficient()
        gini_range = (gini < 1.0) and (gini > 0.0)
        self.assertTrue(gini_range, 'Market Gini Not In Correct Range')

    def test_market_nakamoto(self):
        nakamoto = self.market.get_nakamoto_coefficient()
        nakamoto_range = nakamoto > 0
        self.assertTrue(nakamoto_range, 'Nakamoto Coefficient is Zero')

    def test_market_plot(self):
        plot= self.market.get_plot()
        #self.assertNotEqual(plot_url, '', 'Empty Url String Returned')


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repository = Repository(currency, github_api, github_url, **nakamoto_config)
        
    def test_repository_gini(self):
        gini = self.repository.get_gini_coefficient()
        gini_range = (gini < 1.0) and (gini > 0.0)
        self.assertTrue(gini_range, 'Repository Gini Not In Correct Range')

    def test_repository_nakamoto(self):
        nakamoto = self.repository.get_nakamoto_coefficient()
        nakamoto_range = nakamoto > 0
        self.assertTrue(nakamoto_range, 'Nakamoto Coefficient is Zero')

    def test_repository_plot(self):
        plot = self.repository.get_plot()
        #self.assertNotEqual(plot_url, '', 'Empty Url String Returned')


class TestCustomSector(unittest.TestCase):
    def setUp(self):
        self.custom_sector = CustomSector(random_data, 
                                          currency, 
                                          'custom_sector_type',
                                          **nakamoto_config)

    def test_custom_sector_data(self):
        np_array_type = type(random_data) == np.ndarray
        self.assertTrue(np_array_type, 'Custom Sector Data not a Numpy Array')

    def test_custom_sector_gini(self):
        gini = self.custom_sector.get_gini_coefficient()
        gini_range = (gini < 1.0) and (gini > 0.0)
        self.assertTrue(gini_range, 'Custom Sector Gini Not In Correct Range')

    def test_custom_sector_nakamoto(self):
        nakamoto = self.custom_sector.get_nakamoto_coefficient()
        nakamoto_range = nakamoto > 0
        self.assertTrue(nakamoto_range, 'Nakamoto Coefficient is Zero')

    def test_custom_sector_plot(self):
        plot = self.custom_sector.get_plot()
        self.assertNotEqual(plot, '', 'Empty Url String Returned')


class TestNakamoto(unittest.TestCase):
    def setUp(self):
        self.custom_sector = CustomSector(random_data, 
                                          currency, 
                                          'custom_sector_type',
                                          **nakamoto_config)
        self.custom_sector_2 = CustomSector(random_data_2, 
                                          currency, 
                                          'custom_sector_type',
                                          **nakamoto_config)

        self.geography = Geography(currency, **nakamoto_config)
        self.repository = Repository(currency, github_api, github_url, **nakamoto_config)
        self.market = Market(currency, market_url, **nakamoto_config)
        self.client = Client(currency, **nakamoto_config)
        self.sector_list = [self.geography, 
                            self.market, 
                            self.client, 
                            self.repository, 
                            self.custom_sector,
                            self.custom_sector_2]
        #self.sector_list = [self.custom_sector, self.custom_sector_2]
        self.nakamoto = Nakamoto(self.sector_list)

    def test_nakamoto_summary(self):
        summary = self.nakamoto.get_summary()
        summary_type_check = isinstance(summary, pd.DataFrame)
        self.assertTrue(summary_type_check, 'No Nakamoto Dataframe Summary Returned')

    def test_nakamoto_minimum(self):
        nakamoto = self.nakamoto.get_minimum_nakamoto()
        nakamoto_range = nakamoto > 0
        self.assertTrue(nakamoto_range, 'No Non-Zero Minimum Nakamoto')

    def test_nakamoto_minimum_id(self):
        nakamoto_id = self.nakamoto.get_minimum_nakamoto_id()
        nakamoto_id_string = len(nakamoto_id) > 0
        self.assertTrue(nakamoto_id_string, 'No Minimum Nakamoto ID Returned')

    def test_gini_maximum(self):
        gini = self.nakamoto.get_maximum_gini()
        gini_range = (gini > 0) and (gini < 1)
        self.assertTrue(gini_range, 'Gini Range Out of Bounds')

    def test_gini_maximum_id(self):
        gini_id = self.nakamoto.get_maximum_gini_id()
        gini_id_string = len(gini_id) > 0
        self.assertTrue(gini_id_string, 'No Gini ID Returned')
        

if __name__ == '__main__':
    unittest.main()
