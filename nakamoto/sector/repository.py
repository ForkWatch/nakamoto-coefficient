from .sector import Sector
from nakamoto import SectorNakamoto
from .analysis import Gini, LorenzPlot
from github import Github
import re
import numpy as np

class Repository(Sector):
    def __init__(self, currency, github_api, github_url, **kwargs):
        super(Repository, self).__init__(currency, **kwargs)
        self.type = 'repository'
        self.github_url = self.sanitize_url(github_url)
        self.github_api = github_api
        self.generate_repository_data()

    def sanitize_url(self, github_url_raw):
        github_url = re.sub('https://github.com/', '', github_url_raw)
        github_url_list = github_url.split('/')
        github_string = "/".join(github_url_list[:2])
        return github_string

    def generate_repository_data(self):
        github_object = Github(self.github_api)
        repo = github_object.get_repo(self.github_url)
        contributors = repo.get_contributors()
        stats_contributors = repo.get_stats_contributors()
        contributor_list = [contributor.total for contributor in stats_contributors]
        self.data = np.array(contributor_list)
        gini_object = Gini(self.data)
        self.gini = gini_object.get_gini()
        self.plot = self.generate_lorenz_curve()
        self.nakamoto = self.generate_nakamoto_coefficient()

    def generate_nakamoto_coefficient(self):
        nakamoto_object = SectorNakamoto(self.lorenz_data)
        nakamoto = nakamoto_object.get_nakamoto_coefficient()
        return nakamoto

    def generate_lorenz_curve(self):
        file_name = f'{self.currency}_repository_gini_{self.uuid}'
        lorenz_object = LorenzPlot(self.plotly_username, self.plotly_api_key, self.data, file_name)
        plot_url = lorenz_object.get_plot_url()
        self.lorenz_data = lorenz_object.get_lorenz_data()
        return plot_url
