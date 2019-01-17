from nakamoto import Nakamoto, MinimumNakamoto
from nakamoto.sector import CustomSector, Client, Geography, Market, Repository
import numpy as np

random_data = np.append(np.random.poisson(lam=10, size=40), 
                 np.random.poisson(lam=100, size=10))

client_object = Client(random_data,
                       'ETC',
                       'yazanator90',
                       '0iKTO9Cow8XVEOKklCa3')

client_object.get_gini_coefficient()



