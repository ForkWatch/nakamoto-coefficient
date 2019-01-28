from .sector import Sector
import requests
import json
import pandas as pd
import numpy as np


class Geography(Sector):
    def __init__(self, currency, **kwargs):
        super(Geography, self).__init__(currency, **kwargs)
        self.type = 'geography'
        ether_test = (self.currency == 'ETC') or (self.currency == 'ETH') 
        if ether_test:
            self.generate_evm_geo_data()
        else:
            raise "Node Geography only implemented for EVM-based Nodes"

    def generate_evm_geo_data(self):
        """
            This method aggregates ALL EVM data, not separating them by chain ID.
            So, ETH and ETC data are combined. TODO: Side project to gather this data.
        """
		
		## This URL is the API call ethernodes.org makes to get the node data.
        url = """
		https://www.ethernodes.org/network/1/data?draw=1&columns[0][data]=id&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=host&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=port&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=country&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=clientId&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=client&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=clientVersion&columns[6][name]=&columns[6][searchable]=true&columns[6][orderable]=true&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=os&columns[7][name]=&columns[7][searchable]=true&columns[7][orderable]=true&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=lastUpdate&columns[8][name]=&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&order[0][column]=0&order[0][dir]=asc&start=0&length=1000000&search[value]=&search[regex]=false&_=1545071939943 
      	"""
        
        response = requests.get(url)
        response_hash = json.loads(response.text).get('data')
        df = pd.DataFrame.from_dict(response_hash)
        country_raw = df.groupby('country').nunique()
        country = country_raw['id']
        country = country.sort_values()
        self.data = np.array(country)
