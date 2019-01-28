from .sector import Sector
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
