import json
import plotly.graph_objects as go


class Sankey:
    def __init__(self, plottype='overview'):
        """

        :param type:
        """
        self.plottype=type

    @staticmethod
    def create_sankey():
        """

        :return:
        """
        with open("resources/fig.json", "r") as f:
            fig = go.Figure(json.load(f))
        return fig