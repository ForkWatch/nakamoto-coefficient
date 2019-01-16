class Sector(object):
    def __init__(self):
        self.data = None
        self.graph = None
        self.title = None
        self.currency = None

class Github(Sector):
    def __init__(self):
        super(Sector, self).__init__()
        self.github_url = None
        self.github_api = None

class Market(Sector):
    def __init__(self):
        pass

class Geography(Sector):
    def __init__(self):
        pass

class Client(Sector):
    def __init__(self):
        pass
