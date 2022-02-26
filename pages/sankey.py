import json
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st
from data.data_prep import DataPreparation

class SankeyPage:
    def __init__(self, plottype='overview'):
        """

        :param type:
        """
        self.plottype=plottype
        self.df = SankeyPage.get_data()
        st.title("Bevételek és kiadások")
        st.markdown("Bla bla")
        st.sidebar.title("Szűrés")
        self.select_year = st.sidebar.selectbox('Valasszon egy évet:', self.df['Év'])

    def run(self):
        fig = self.create_sankey(self.df)
        st.write(fig)

    @staticmethod
    def get_data():
        """

        :return:
        """
        data = DataPreparation('resources', 'bevetelek_2017_2021.csv', 'kiadasok_2017_2021.csv', 'UTF-8', ';', 'sankey')
        df = data.run()
        return df

    def create_sankey(self):
        """

        :return:
        """
        df_ev = self.df[self.df['Év'] == self.select_year]

        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=["A1", "A2", "B1", "B2", "C1", "C2"],
                color="blue"
            ),
            link=dict(
                source=[0, 1, 0, 2, 3, 3],  # indices correspond to labels, eg A1, A2, A1, B1, ...
                target=[2, 3, 3, 4, 4, 5],
                value=[8, 4, 2, 8, 4, 2]
            ))])

        st.write(fig)
