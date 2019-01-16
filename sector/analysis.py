from decimal import Decimal
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

class Gini(object):
    def __init__(self, data_array):
        self.data_array = data_array
        self.gini_coefficient = self.generate_gini()

    def generate_gini(self):
        n = len(self.data_array)
        coefficient = Decimal(2. / n)
        constant = Decimal((n + 1.) / n)
        weighted_sum = sum([(index + 1) * item for index, item in enumerate(contributor_array)])
        gini = coef_*weighted_sum/(contributor_array.sum()) - const_
        return gini

    def get_gini(self):
        return self.gini_coefficient

class LorenzPlot(object):
    def __init__(self, plotly_username, plotly_api_key, data_array, file_name):
        self.plotly_username = plotly_username
        self.plotly_api_key = plotly_api_key
        self.data_array = data_array
        self.file_name = file_name
        self.lorenz_data = self.generate_lorenz_curve()
        self.plotly_url = self.get_plot_url()

    def generate_lorenz_curve(self):
        data_copy = data_array.copy()
        lorenz = data_copy.cumsum() / data_copy.sum()
        lorenz = np.insert(lorenz, 0, 0)
        lorenz = lorenz.astype(float)
        return lorenz

    def plotly_url(self):
        plotly.tools.set_credentials_file(username=self.plotly_username, api_key=self.plotly_api_key)

        trace = go.Scattergl(
            x = np.arange(self.lorenz_data.size)/(self.lorenz_data.size-1),
            y = self.lorenz_data,
            mode = 'markers'
        )

        trace2 = go.Scatter(
            x = [0,1],
            y = [0,1]
        )

        data = [trace, trace2]
        plot_url = py.plot(data, filename=self.file_name)
        return plot_url
