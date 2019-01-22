from nakamoto import SectorNakamoto, MinimumNakamoto
from nakamoto.sector import CustomSector, Client, Geography, Market, Repository
import numpy as np

random_data = np.append(np.random.poisson(lam=10, size=40), 
                 np.random.poisson(lam=100, size=10))

client_object = Client(random_data,
                       'ETC',
                       'yazanator90',
                       '0iKTO9Cow8XVEOKklCa3')

print(client_object.get_nakamoto_coefficient())

github_object = Repository(random_data,
                       'ETC',
                       'yazanator90',
                       '0iKTO9Cow8XVEOKklCa3',
                       '94a0092711bbf59ac07493b803363638fd2de096',
                       'https://github.com/input-output-hk/mantis')

print(github_object.get_nakamoto_coefficient())
