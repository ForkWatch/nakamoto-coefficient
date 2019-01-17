from sector import Sector
from analysis import Gini, LorenzPlot
from requests_html import HTMLSession

class Market(Sector):
    def __init__(self, market_url):
        super(Sector, self).__init__()
        self.market_url = market_url
        self.generate_market_data()
        
    def generate_market_data(self):
        session = HTMLSession()
        r = session.get(self.market_url)
        table = r.html.find('#markets-table', first=True)
        market_df = pd.read_html(table.html)[0]
        volume_data = market_df['Volume (24h)']
        volume_data = volume_data.str.replace('$', '', regex=False)
        volume_data = volume_data.str.replace('**', '', regex=False)
        volume_data = volume_data.str.replace(',', '', regex=False)
        volume_data = pd.to_numeric(volume_data)
        volume_data = volume_data.sort_values()
        gini_object = Gini(volume_data)
        self.gini = gini_object.get_gini()
        self.plot = self.generate_lorenz_curve()

    def generate_lorenz_curve(self):
        file_name = f'{self.currency}_exchanges_gini_{self.uuid}'
        lorenz_object = LorenzPlot(self.plotly_username, self.plotly_api, self.volume_data, file_name)
        plot_url = lorenz_object.plotly_url()
        return plot_url
