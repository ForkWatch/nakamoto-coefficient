class Sector(object):
    def __init__(self):
        self.data = None
        self.graph = None
        self.title = None
        self.currency = None
        self.gini = None

    def get_gini(self):
        if self.gini:
            return self.gini

    def get_graph_url(self):
        if self.graph:
            return self.graph

class Market(Sector):
    def __init__(self):
        pass

class Geography(Sector):
    def __init__(self):
        pass

class Client(Sector):
    def __init__(self):
        pass
