from decimal import Decimal
import plotly
import plotly.graph_objs as go
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


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
    def __init__(self, plot_notebook, plot_image_path, data_array, file_name, title):
        self.plot_notebook = plot_notebook
        self.plot_image_path = plot_image_path
        self.data_array = data_array
        self.file_name = file_name
        self.title = title
        self.lorenz_data = self.generate_lorenz_curve()

    def generate_lorenz_curve(self):
        data_copy = self.data_array.copy()
        lorenz = data_copy.cumsum() / data_copy.sum()
        lorenz = np.insert(lorenz, 0, 0)
        lorenz = lorenz.astype(float)
        return lorenz

    def get_lorenz_data(self):
        return self.lorenz_data

    def generate_plot(self):
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
                        title='Distribution'
                    ),
        )

        data = [trace, trace2, trace3]
        figure = go.Figure(data=data, layout=layout)
        return figure

    def get_plot(self):
        figure = self.generate_plot()
        init_notebook_mode(connected=True)
        if self.plot_notebook and self.plot_image_path:
            plot(figure, image='png', image_filename=self.plot_image_path)
            iplot(figure, image='png', filename=self.plot_image_path)
        elif self.plot_notebook:
            iplot(figure)
        elif self.plot_image_path:
            plot(figure, image='png', filename=self.plot_image_path)
        else:
            raise Exception("No Image File Path specified for Plot Generation. Must pass plot_image_path")
