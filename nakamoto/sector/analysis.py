from decimal import Decimal
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np


class Gini(object):
    def __init__(self, data_array):
        self.data_array = data_array
        self.gini_coefficient = self.generate_gini()

    def generate_gini(self):
        n = len(self.data_array)
        coefficient = Decimal(2. / n)
        constant = Decimal((n + 1.) / n)
        weighted_sum = sum([(index + 1) * item for index, item in enumerate(self.data_array)])
        gini = coefficient * weighted_sum / (self.data_array.sum()) - constant
        return float(gini)

    def get_gini(self):
        return self.gini_coefficient


class LorenzPlot(object):
    def __init__(self, plotly_username, plotly_api_key, data_array, file_name, title):
        self.plotly_username = plotly_username
        self.plotly_api_key = plotly_api_key
        self.data_array = data_array
        self.file_name = file_name
        self.title = title
        self.lorenz_data = self.generate_lorenz_curve()
        self.plotly_url = None 

    def generate_lorenz_curve(self):
        data_copy = self.data_array.copy()
        lorenz = data_copy.cumsum() / data_copy.sum()
        lorenz = np.insert(lorenz, 0, 0)
        lorenz = lorenz.astype(float)
        return lorenz

    def get_lorenz_data(self):
        return self.lorenz_data

    def generate_plot_url(self):
        plotly.tools.set_credentials_file(username=self.plotly_username, api_key=self.plotly_api_key)
        color = np.array(['rgb(255,255,255)'] * self.lorenz_data.shape[0])
        color[self.lorenz_data < 0.51] = 'blue'
        color[self.lorenz_data >= 0.51] = 'red'

        trace = go.Bar(
            x = np.arange(self.lorenz_data.size)/(self.lorenz_data.size-1),
            y = self.lorenz_data,
            name = 'Lorenz Curve',
            marker=dict(color=color.tolist())
        )

        trace2 = go.Scatter(
            x = [0,1],
            y = [0,1],
            name = 'Equality Line'
        )

        trace3 = go.Scatter(
            x = [0, 1],
            y = [0.51, 0.51],
            name = '51% Cutoff'
        )

        layout = go.Layout(
                    title=self.title,
                    xaxis=dict(
                        title='Entities'
                    ),
                    yaxis=dict(
                        title='Percentage Ownership'
                    ),
        )

        data = [trace, trace2, trace3]
        figure = go.Figure(data=data, layout=layout)
        plot_url = py.plot(figure, filename=self.file_name, auto_open=False)
        return plot_url

    def get_plot_url(self):
        if not self.plotly_url:
            self.plotly_url = self.generate_plot_url()
        return self.plotly_url
