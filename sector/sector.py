class Sector(object):
    def __init__(self):
        self.data = None
        self.plot = None
        self.title = None
        self.currency = None
        self.gini = None

    def get_gini_coefficient(self):
        if self.gini:
            return self.gini

    def get_plot_url(self):
        if self.plot:
            return self.plot

class Geography(Sector):
    def __init__(self):
        pass

class Client(Sector):
    def __init__(self):
        pass
