from sector import Sector
from analysis import Gini
from github import Github
import re

class Repository(Sector):
    def __init__(self, github_api, github_url, plot_title):
        super(Sector, self).__init__()
        self.github_url = self.sanitize_url(github_url) 
        self.github_api = github_api
        self.generate_repository_data()

    def sanitize_url(self, github_url_raw):
        github_url = re.sub('https://github.com/', '', github_url_raw)
        github_url_list = github_url.split('/')
        github_string = "".join(github_url_list[:2])
        return github_string

    def generate_repository_data(self):
        github_object = Github(github_api)
        repo = github_object(self.github_url)
        contributors = repo.get_contributors()
        stats_contributors = repo.get_stats_contributors()
        contributor_list = [contributor.total for contributor in stats_contributors]
        contributor_data = np.array(contributor_list)
        gini_object = Gini(contributor_data)
        self.gini = gini_object.get_gini()

    def gini_coefficient(self):
        if self.gini:
            return self.gini

